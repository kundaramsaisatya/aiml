# AI-Powered Tic Tac Toe using Q-Learning

## Overview

This project is an AI-powered Tic Tac Toe game where a human competes against an intelligent computer opponent. The AI is developed using the Q-Learning algorithm, a Reinforcement Learning technique that enables an agent to learn optimal actions through repeated gameplay.

The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

---

## Objectives

* Build a Human vs AI Tic Tac Toe game.
* Demonstrate Reinforcement Learning using Q-Learning.
* Provide an interactive web-based interface.
* Understand how an AI agent learns through rewards and penalties.

---

## Technologies Used

Frontend

* HTML
* CSS
* JavaScript

Backend

* Python
* Flask

Machine Learning

* Reinforcement Learning
* Q-Learning

Libraries

* Flask
* NumPy
* Pickle

---

## Project Structure

```text
tic-tac-toe-ai/
│
├── app.py
├── train.py
├── q_table.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## How the Project Works

The project is divided into two main phases.

### Phase 1: Training the AI

The AI is first trained before the game is played.

The training program performs thousands of simulated Tic Tac Toe games.

For every game:

1. The board starts empty.
2. The AI selects moves.
3. Rewards are assigned:

   * Win = Positive reward
   * Draw = Small reward
   * Loss = Negative reward
4. The Q-values are updated.
5. The learned values are stored inside a Q-Table.

After training completes, the Q-Table is saved as:

```text
q_table.pkl
```

This file stores the AI's learned knowledge.

---

### Phase 2: Playing the Game

When the Flask application starts:

1. The trained Q-Table is loaded.
2. The player opens the web application.
3. The player clicks a square.
4. The updated board is sent to Flask.
5. Flask searches the Q-Table.
6. The AI chooses the move with the highest learned reward.
7. The move is returned to the browser.
8. The board is updated.

This process repeats until someone wins or the game ends in a draw.

---

## Q-Learning Concept

Q-Learning is a Reinforcement Learning algorithm.

Instead of following predefined rules, the AI gradually learns which moves produce better outcomes.

The AI learns from:

* Current board state
* Possible actions
* Reward received after each action

Over many training games, the AI improves its decision making.

---

## Reward System

The AI learns using rewards.

* Win → +1
* Draw → +0.5
* Loss → -1

Higher rewards encourage stronger moves, while penalties discourage poor decisions.

---

## Game Flow

1. User opens the application.
2. Human makes a move.
3. The board is sent to Flask.
4. Flask loads the learned Q-values.
5. AI selects the best move.
6. AI returns the selected position.
7. Board updates.
8. Winner is checked.
9. Game continues until completion.

---

## Features

* Human vs AI gameplay
* Q-Learning based decision making
* Interactive web interface
* Scoreboard
* Restart game functionality
* Win and draw detection
* Flask backend
* Responsive user interface

---

## Advantages

* Demonstrates Reinforcement Learning concepts.
* Easy to understand.
* Interactive gameplay.
* Suitable for AI/ML coursework.
* Modular project structure.

---

## Future Improvements

* Train the AI for more episodes.
* Add multiple difficulty levels.
* Improve the Q-Learning implementation.
* Store player statistics.
* Add animations and sound effects.
* Deploy the application online.

---

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Train the AI:

```bash
python train.py
```

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project we learned:

* Fundamentals of Reinforcement Learning.
* Implementation of Q-Learning.
* Web development using Flask.
* Frontend and backend integration.
* Handling game logic.
* Designing an AI-powered interactive application.

---

## Conclusion

This project demonstrates how Reinforcement Learning can be applied to game development. By training the AI using Q-Learning, the system learns to make increasingly better decisions over time. The combination of Flask, Python, HTML, CSS, and JavaScript provides a complete end-to-end AI application that showcases both machine learning concepts and full-stack web development.
