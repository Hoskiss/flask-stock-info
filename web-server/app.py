from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hi")
def yanwei():
    return "Hello, There"

if __name__ == "__main__":
    app.run(debug=True)
