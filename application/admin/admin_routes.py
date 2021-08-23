from flask import Blueprint, render_template, flash, session, Flask

admin = Blueprint('admin', __name__, template_folder='../assets/templates/admin', static_folder='../assets/static', url_prefix='/admin')

from app import mysql

@admin.route('/')
def test():
    return render_template('add_books.html')

@admin.route('/add')
def add_books():
    query=('''select * from frappe.books''')
    testquery= mysql.query_db(query)
    return render_template('add_books.html',testquery=testquery)