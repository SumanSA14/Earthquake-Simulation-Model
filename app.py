from flask import Flask, render_template, jsonify
import simulation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    data = simulation.run_simulation()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)