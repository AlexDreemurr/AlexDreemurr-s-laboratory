from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

name = "AlexDreemurr"
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

@app.route("/")
def index():
    return render_template("blog1.html", name = name, friends = friends)

app.run()

