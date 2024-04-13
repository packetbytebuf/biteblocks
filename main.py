from flask import Flask, render_template, send_file

app = Flask("byteblox")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/puzzle.css")
def css():
    return send_file("./templates/puzzle.css")

@app.route("/puzzle.js")
def js():
    return send_file("./templates/puzzle.js")

@app.route("/images/<filename>") # this is fucking stupid just like me
def images(filename):
    return send_file("./templates/images/"+filename)

app.run("0.0.0.0",5000)

while True:
    pass