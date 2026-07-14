from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open("q_table.pkl", "rb") as f:
    q_table = pickle.load(f)


def board_to_state(board):
    return "".join(board)


def available_moves(board):
    return [i for i, x in enumerate(board) if x == " "]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ai_move", methods=["POST"])
def ai_move():

    data = request.get_json()
    board = data["board"]

    state = board_to_state(board)

    moves = available_moves(board)

    if not moves:
        return jsonify({"move": -1})

    if state in q_table:
        values = q_table[state]
        move = max(moves, key=lambda x: values[x])
    else:
        move = moves[0]

    return jsonify({"move": move})


if __name__ == "__main__":
    app.run(debug=True)