"""
Database Model interface for the COMP249 Web Application assignment

@author: steve cassidy
"""
import sqlite3
import time

def position_list(db, limit=10):
    """Return a list of positions ordered by date
    db is a database connection
    return at most limit positions (default 10)

    Returns a list of tuples  (id, timestamp, owner, title, location, company, description)
    """

    # query the records in db and sorted them by time, and limited by a given number (stored in the parameter limit).
    cursor = db.cursor()
    cursor.execute("SELECT id, timestamp, owner, title, location, company, description FROM positions ORDER BY timestamp DESC LIMIT 0,?", (limit,))

    # return all the query results.
    return cursor.fetchall()


def position_get(db, id):
    """Return the details of the position with the given id
    or None if there is no position with this id

    Returns a tuple (id, timestamp, owner, title, location, company, description)

    """
    cursor = db.cursor()
    cursor.execute("SELECT id, timestamp, owner, title, location, company, description FROM positions WHERE id=?", (id,))

    return cursor.fetchone()



def position_add(db, usernick, title, location, company, description):
    """Add a new post to the database.
    The date of the post will be the current time and date.
    Only add the record if usernick matches an existing user

    Return True if the record was added, False if not."""

    cursor = db.cursor()

    # if there is no record can match the input usernick, we should return false.
    cursor.execute("SELECT * FROM positions WHERE owner=\'" + usernick + "\'")
    if cursor.fetchone() is None:
        return False

    # get the maximum id in the database so that we can determine the id of new record.
    cursor.execute("SELECT MAX(\"id\") FROM positions")
    id = cursor.fetchone()[0] + 1

    # calculate timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # add the new record into database
    cursor.execute("INSERT INTO positions VALUES (?, ?, ?, ?, ?, ?, ?)", (id, timestamp, usernick, title, location, company, description))
    db.commit()

    return True


