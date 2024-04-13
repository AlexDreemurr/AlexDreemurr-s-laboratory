from flask import Flask, request, url_for, redirect, render_template
from markupsafe import escape
import time

app = Flask(__name__)

myname = "AlexDreemurr"
friends = ["KiraRettosei",
           "Akari",
           "Yukii",
           "David",
           "Hank",
           "December",
           "Derek"]

'''
@app.route('/user/<name>')
def hello(name):
    return f'User:{escape(name)}'
app.run()
'''

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        print(name, message)
        with open("messages.txt", "a") as file:
            localtime = time.asctime( time.localtime(time.time()) )
            file.write(f"{localtime} {name}::{message}\n")

    return render_template("blog1.html", name = myname, friends = friends)

app.run(host = "172.20.10.2", port=5000)

