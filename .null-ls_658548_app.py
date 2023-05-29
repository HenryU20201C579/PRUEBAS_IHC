from flask import Flask, render_template, request, redirect
from flask.cli import main
from flask_mysqldb import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)
# mysql = MySQL()
#
# app.config['MYSQL_DATABASE_HOST'] = '3.208.8.94'
# app.config['MYSQL_DATABASE_USER'] = 'support'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'sistema.db'
# app.config['MYSQL_DATABASE_DB'] = 'tb3'
# mysql.init_app(app)
#
#


@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
