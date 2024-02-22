# Tetrabot

<strong> Disclaimer </strong> - this project is quite old now (about 2 years); it's one of the first projects that I ever worked on completely from scratch without a tutorial or guide. The code style isn't great as I was new to Python (and large-scale software development in general) back then, but I'm still happy with the final result and wanted to share!

Demo: https://www.youtube.com/watch?v=5iMoquDzvVA

Tetrabot is a bot that I coded to play Tetris on the website tetr.io. It is able to play at a rate of over 4 pieces per second, while choosing fairly optimal piece placements. Here's an overview of the parts:

<strong> main.py </strong>- Puts all the different parts together, calling methods in the other files to gather information about the upcoming piece shape, try various placements, select the best one, and make the key inputs to place the piece.

<strong> checkQueue.py </strong>- Uses Python Imaging Library to check the color of the pixels where the next piece appears. Using this color data, it determines which of the 7 Tetris piece shapes the next piece is.

<strong> tryPlacement.py </strong>- Simulates placing the piece in all the possible placements (up to 10 horizontal placements, and 4 possible rotations). The script always keeps track of what the current board state is, and uses that to see what the board state would look like if a piece is placed in a certain spot.

<strong> evaluateBoard.py </strong>- Given a board state, it assigns a score to the state (where higher is better) using an easily customizable heuristic. This includes factors like how many holes are formed in the board, how many lines are cleared, how "smooth" the board is, and more. The weighting of each factor can easily be customized. The score returned by this method is used to pick which placement is the best, in the eyes of the bot.

<strong> placePiece.py </strong>- Uses the pynput library to actually make the keypresses necessary to place the piece in the placement that was calculated to be the best.
