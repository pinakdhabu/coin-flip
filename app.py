from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    result = random.choice(["Heads", "Tails"])
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
