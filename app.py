import os
from flask import Flask, flash, redirect, render_template, request, session

# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from werkzeug.security import check_password_hash, generate_password_hash
import logging

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
categories= [] # Categories in the list
title = [] # Initializing place to store title
users = [] # Making a list where key value pairs will be kept

@app.route("/", methods=["GET", "POST"])
def hello():

    if request.method == "POST":
        
        title.append(request.form.get("title"))

        for x in range(30):
            if request.form.get(str(x)) == None:
                exit
            else:
                categories.append(request.form.get(str(x)))
        
        return render_template("list.html", title=title, categories=categories)

    else:
        return render_template("landing.html")


@app.route("/list", methods=["GET", "POST"])
def list():
    
    if request.method == "POST":
        username = request.form.get("username")
        userCat = request.form['category']
        users.append({
            'Name': request.form.get("username"),
            'Category': userCat,
            })
        
        return render_template("list.html", title=title, categories=categories, users=users)

    else:
        return render_template("list.html")

