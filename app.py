from flask import Flask
from application.mysqlconnection import MySQLConnector


app = Flask(__name__)
mysql = MySQLConnector(app,'frappe')
from application.admin.admin_routes import admin
from application.user.user_routes import user
app.register_blueprint(admin)
app.register_blueprint(user)
app.config['SECRET_KEY'] = 'its my secret key'
app.config['TESTING'] = True
app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run()














