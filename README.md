# U.S. States Guessing Game

An interactive geography learning game where players test their knowledge of U.S. states by guessing state names and seeing them appear on the map.

## Features

- Interactive map of the United States
- Type in state names to mark them on the map
- Score tracking showing how many states you've correctly identified
- Exit option to quit the game at any time
- Learning tool: generates a CSV list of states you missed for future study
- Clean, minimalist design focused on geography learning

## How to Play

1. Run the game using Python
2. Type in the name of a U.S. state when prompted
3. If correct, the state will be labeled on the map and your score will increase
4. Continue guessing states until you've found all 50
5. Type "Exit" to quit the game anytime
6. When exiting, a CSV file will be generated with states you haven't guessed

## Installation

1. Clone this repository
2. Make sure you have Python installed (Python 3.6 or higher recommended)
3. Install required packages:

**pip install pandas**

4. Run the game:

**python main.py**


## Project Structure

- `main.py` - Main game script
- `50_states.csv` - Data file containing state names and coordinates
- `blank_states_img.gif` - Map image of the United States
- `states_to_learn.csv` - Generated file of states you need to study

## Technologies Used

- Python 3
- Turtle Graphics library for UI
- Pandas for data management
- CSV data storage

## Future Improvements

- Add difficulty levels (e.g., timer, hints)
- Include state capitals as an additional learning element
- Add sound effects for correct/incorrect guesses
- Create a web-based version