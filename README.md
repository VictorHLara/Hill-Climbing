# Hill Climbing with Pygame

This project implements a hill climbing algorithm in a 2D discrete space using the Pygame library for visualization.

## Description

The hill climbing algorithm is used to find the local maximum or minimum in a list of values. The visualization displays columns representing the values and shows the agent moving from column to column until it finds the local maximum or minimum.

## How It Works

1. **Initial Setup**: The screen is set up with columns representing the values in the list.
2. **User Interaction**: The user starts the search by pressing the `SPACE` key.
3. **Algorithm Execution**: The agent moves from one column to another, following the path calculated by the hill climbing algorithm.
4. **Visualization**: During the search, the agent's current column is highlighted. When the local maximum is found, it is labeled "Local Max".

## Requirements

- Python 3.x
- Pygame

## How to Run

1. Install the dependencies:
    ```bash
    pip install pygame
    ```
2. Run the script:
    ```bash
    python main.py
    ```

##Visualization:
