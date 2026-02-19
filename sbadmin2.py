#!/usr/bin/env python
from flask import Flask, url_for, render_template
import jinja2.exceptions
from db import Database

db = Database()
db.setup_customers_table()
admins = db.GetAdmins()
customers = db.Get_All_Customers()
args = {"admins":admins,
        "coder":"silvijn",
        "customers": customers,
    "date":"Woensdag 21 Januari 15:00"}


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', args=args)

@app.route('/<pagename>')
def admin(pagename):
    return render_template(pagename+'.html', args=args)

@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(e):
    return not_found(e)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)