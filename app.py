from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return "<h1>Welcome to te Login Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    

    