"""
Created on Mar 26, 2012

@author: steve
"""
from database import password_hash
from bottle import response, request
from random import Random

# this variable MUST be used as the name for the cookie used by this application
COOKIE_NAME = 'sessionid'


def random_str(length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

    random = Random()

    for i in range(length):
        str += chars[random.randint(0, len(chars) - 1)]

    return str


def check_login(db, usernick, password):
    """returns True if password matches stored"""

    # query the record with specific user name and password hash.
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE password=? AND (UPPER(nick) LIKE UPPER(?));", (password_hash(password), usernick))

    # if the record existed, return true, otherwise, return false
    if len(cursor.fetchall()) > 0:
        return True
    else:
        return False

def generate_session(db, user_name):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    cursor = db.cursor()

    # check the given usernick. if it is not registered, return None
    cursor.execute("SELECT * FROM positions WHERE owner=?;", (user_name,))
    if cursor.fetchone() is None:
        return None

    # check if there is a existed session for the given user
    cursor.execute("SELECT * FROM sessions WHERE usernick=?;", (user_name,))
    row = cursor.fetchone()

    # if find the existed session, reuse it, otherwise, generate a new one.
    if row is not None:
        session_id = row[0]
        response.set_cookie(COOKIE_NAME, session_id)
    else:
        session_id = random_str(16)
        cursor.execute("INSERT INTO sessions VALUES (?,?)", (session_id, user_name))
        db.commit()

    response.set_cookie(COOKIE_NAME, session_id)


def delete_session(db, user_name):
    """remove all session table entries for this user"""
    cursor = db.cursor()
    cursor.execute("DELETE FROM sessions WHERE usernick=(?);", (user_name,))
    db.commit()

def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""

    # get the active session id
    cookie = request.get_cookie(COOKIE_NAME)

    # query the corresponding user name
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sessions WHERE sessionid=?;", (cookie,))
    record = cursor.fetchone()

    if record is not None:
        return record[1]
    else:
        return None


