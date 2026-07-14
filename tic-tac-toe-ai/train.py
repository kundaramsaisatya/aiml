import random
import pickle

LEARNING_RATE = 0.8
DISCOUNT = 0.95
EPSILON = 0.2
EPISODES = 50000

q_table = {}


def state_to_string(board):
    return "".join(board)


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == " "]


def winner(board):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None


for episode in range(EPISODES):

    board = [" "] * 9
    history = []

    while True:

        state = state_to_string(board)

        if state not in q_table:
            q_table[state] = [0] * 9

        moves = available_moves(board)

        if random.random() < EPSILON:
            move = random.choice(moves)
        else:
            values = q_table[state]
            move = max(moves, key=lambda x: values[x])

        board[move] = "X"

        history.append((state, move))

        result = winner(board)

        if result:

            reward = 0

            if result == "X":
                reward = 1
            elif result == "Draw":
                reward = 0.5
            else:
                reward = -1

            for s, m in reversed(history):
                q_table[s][m] += LEARNING_RATE * (
                    reward - q_table[s][m]
                )
                reward *= DISCOUNT

            break

        opponent = random.choice(available_moves(board))
        board[opponent] = "O"

        result = winner(board)

        if result:

            reward = -1 if result == "O" else 0.5

            for s, m in reversed(history):
                q_table[s][m] += LEARNING_RATE * (
                    reward - q_table[s][m]
                )
                reward *= DISCOUNT

            break

with open("q_table.pkl", "wb") as f:
    pickle.dump(q_table, f)

print("Training Complete!")
print("States Learned:", len(q_table))