from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def ninja():
    color="ninja"
    return render_template('ninja.html',color=color)
@app.route('/ninja/<color>')
def display_ninja(color):
    print color
    return render_template("ninja.html", color=color)
app.run(debug=True)
