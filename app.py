from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/contact/")
def contact():
    return "<h1>Hello contact</h1>"
 
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/user/<name>/")
def user(name):
    return f"Hello {name}"

@app.route("/perso/<name>/")
def perso(name):
    return render_template("perso.html",username=name)

if __name__ == "__main__" :
    app.run(debug=True)