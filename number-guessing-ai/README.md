# AI Number Guessing Game

## Overview

The AI Number Guessing Game is an interactive web application where the user thinks of a number between 1 and 100, and the AI attempts to guess it. After each guess, the user provides feedback indicating whether the guess is too high, too low, or correct.

The AI continuously narrows the search range based on the user's feedback until it successfully guesses the number.

The application is developed using Flask for the backend and HTML, CSS, and JavaScript for the frontend.

---

## Objectives

* Build an interactive Human vs AI number guessing game.
* Demonstrate intelligent decision-making.
* Implement an efficient search strategy.
* Develop a responsive web application using Flask.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI Technique

* Intelligent Search
* Binary Search Strategy

---

## Project Structure

```text
number-guessing-ai/
│
├── app.py
├── ai.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## How the Project Works

The game follows a simple interaction between the human and the AI.

### Step 1

The user thinks of a secret number between 1 and 100.

### Step 2

The AI makes an initial guess.

Example:

```text
AI Guess: 50
```

### Step 3

The user provides one of three responses:

* Too Low
* Too High
* Correct

### Step 4

The AI updates its search range.

For example:

* Guess = 50
* User says "Too Low"

New range:

```text
51 - 100
```

The AI then makes another guess using the updated range.

This process continues until the correct number is found.

---

## AI Decision Process

The AI maintains three values:

* Lowest possible number
* Highest possible number
* Current guess

After every response:

If the guess is too low:

```text
low = guess + 1
```

If the guess is too high:

```text
high = guess - 1
```

The next guess is calculated as:

```text
guess = (low + high) // 2
```

This allows the AI to eliminate half of the remaining possibilities after every attempt.

---

## Game Flow

```text
User Thinks of a Number
          │
          ▼
AI Makes a Guess
          │
          ▼
User Gives Feedback
          │
          ▼
Update Search Range
          │
          ▼
Generate Next Guess
          │
          ▼
Repeat Until Correct
```

---

## Features

* Human vs AI gameplay
* Intelligent guessing strategy
* Attempt counter
* Restart game option
* Responsive web interface
* Fast and efficient guessing
* Flask backend

---

## Advantages

* Simple and interactive.
* Demonstrates intelligent search.
* Easy to understand.
* Suitable for beginners.
* Clean project structure.

---

## Time Complexity

The AI uses Binary Search.

Worst-case complexity:

```text
O(log n)
```

For numbers between 1 and 100, the AI requires at most 7 guesses to identify the correct number.

---

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project we learned:

* Flask web development
* Frontend and backend communication
* Intelligent search algorithms
* Binary Search implementation
* State management
* Interactive web application development

---

## Future Improvements

* Add multiple difficulty levels.
* Allow custom number ranges.
* Maintain a leaderboard.
* Store previous game history.
* Add sound effects and animations.
* Support voice commands.
* Add multiplayer mode.

---

## Conclusion

The AI Number Guessing Game demonstrates how an intelligent search strategy can efficiently solve a problem by reducing the search space after every user response. Although this project uses Binary Search rather than machine learning, it showcases how AI can make informed decisions based on feedback and provides a strong foundation for understanding intelligent problem-solving techniques.
