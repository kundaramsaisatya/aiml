from flask import Flask, render_template, request, jsonify
from ai import NumberGuessAI

app = Flask(__name__)

ai = NumberGuessAI()


@app.route("/")
def home():
    ai.reset()
    return render_template("index.html")


@app.route("/guess")
def guess():
    return jsonify({
        "guess": ai.get_guess(),
        "attempts": ai.get_attempts()
    })


@app.route("/feedback", methods=["POST"])
def feedback():

    data = request.get_json()

    action = data["action"]

    if action == "low":
        ai.too_low()

    elif action == "high":
        ai.too_high()

    elif action == "reset":
        ai.reset()

    return jsonify({
    "guess": ai.get_guess(),
    "attempts": ai.get_attempts()
    })


if __name__ == "__main__":
    app.run(debug=True)