## Tic Tac Toe vs AI (Minimax Algorithm)
## Project Overview

This project is a Tic Tac Toe game with an AI opponent built using Python.
The AI uses the Minimax Algorithm, which ensures that it always makes the best possible move.

## The result: The AI is unbeatable — 
it will either win:
![Game Board](https://github.com/ChandramoulixGamer/Tic-Tac-Toe-vs-Unbeatable-AI/blob/263fa397d4bf74dac557e26db3fe550e1edf79d9/Screenshot%202026-03-28%20194405.png )

or draw 
![Game Board](https://github.com/ChandramoulixGamer/Tic-Tac-Toe-vs-Unbeatable-AI/blob/263fa397d4bf74dac557e26db3fe550e1edf79d9/Screenshot%202026-03-28%20194441.png)

but never lose.

## Objective

Develop a Tic Tac Toe game with an intelligent AI opponent
Implement the Minimax algorithm for optimal decision-making
Understand how AI works in simple game environments

## Technologies Used

Python (3.x)
Pygame (for game interface)
NumPy (for board representation)
Visual Studio Code (IDE)

## How the AI Works (Minimax Algorithm)

The Minimax algorithm works by:

Simulating all possible future moves
Evaluating each outcome:
Win → +10
Loss → -10
Draw → 0
Choosing the move that gives the best possible result

AI = Maximizing player
Human = Minimizing player

This guarantees perfect gameplay

## Features
Play against an unbeatable AI
Simple and clean game interface using Pygame
Detects:
Win
Loss
Draw

## How to Run the Project

1. Clone the Repository
git clone https://github.com/your-username/tic-tac-toe-ai.git
cd tic-tac-toe-ai
2. Install Dependencies
pip install pygame numpy
3. Run the Game
python main.py

## Project Structure
tic-tac-toe-ai/
│── main.py
│── README.md
│── images/

## Author

Chandramouli Gangopadhyay
B.Tech CSE 5 th Sem 

## Future Improvements

Add Alpha-Beta Pruning for optimization
Improve UI/UX design
Add difficulty levels
Extend to larger boards (4x4, etc.)

## Conclusion

This project demonstrates how AI decision-making works using Minimax.
It’s a great example of applying game theory and recursion in a practical way.)

