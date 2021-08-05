from flaskext.mysql import MySQL
from flask import Flask, render_template
# from flask.templating import render_template
app = Flask(__name__)



@app.route('/')
def dashboard():
    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)