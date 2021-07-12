import os
from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from werkzeug.security import check_password_hash, generate_password_hash

#Initialize application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Ensure responses arent cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        
        title = request.form.get("title")
        number = int(request.form.get("number_categories"))

        return render_template("list_settings.html", title=title, number=number)

    else:
        return render_template("landing.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        
        title = request.form.get("title")
        number = int(request.form.get("number_categories"))

        return render_template("list_settings.html", title=title, number=number)

    else:
        return render_template("landing.html")
