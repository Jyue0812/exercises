from . import home

@home.route("/home/")
def home():
    return "<h1 style='color:green'>home page</h1>"