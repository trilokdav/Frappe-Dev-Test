from flaskext.mysql import MySQL
from flask import Flask, render_template, session, flash
app = Flask(__name__)
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'frappe')


@app.route('/')
def dashboard():
    query=('''select * from frappe.books''')
    testquery= mysql.query_db(query)
    print(testquery)
    return render_template('index.html',testquery=testquery)


@app.route('/add-books')
def add_books():
    query=('''select * from frappe.books''')
    testquery= mysql.query_db(query)
    return render_template('add_books.html',testquery=testquery)





if __name__ == "__main__":
    app.run(debug=True)