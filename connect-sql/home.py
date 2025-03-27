from flask import Flask, render_template, request , redirect
import mysql.connector
App = Flask(__name__)


con = mysql.connector.connect(
    host="localhost",
    user="hari",
    password="hari123",
    database="hari"

)
con.autocommit= True
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT,age int)")


@App.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        print(name,age)
        cur = con.cursor()
        cur.execute("INSERT INTO users (name,age) VALUES (%s,%s)",(name,age))

        return redirect("/")

    return render_template('index.html')

App.run()