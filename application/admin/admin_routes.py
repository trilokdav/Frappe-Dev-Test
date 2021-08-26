from flask import Blueprint, render_template, flash, session, request
admin = Blueprint('admin', __name__, template_folder='../assets/templates/admin', static_folder='../assets/static', url_prefix='/admin')
from app import mysql



@admin.route('/')
def test():
    return render_template('dashboard.html')

@admin.route('/books')
def books():
    query=('''select * from frappe.books''')
    testquery= mysql.query_db(query)
    return render_template('books.html',testquery=testquery)


@admin.route('/import-books')
def import_books():
    pass
