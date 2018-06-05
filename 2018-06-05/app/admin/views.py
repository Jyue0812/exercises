from . import admin

@admin.route("/admin/")
def admin():
    return "<h1 style='color:green'>admin page</h1>"