# Toy Robot Simulator

This is a simple toy robot simulator. The robot can be placed on a table, moved around, and report its position and facing direction. The project includes a main script `ToyRobot.py` and a test script `test_ToyRobot.py` using `pytest`.

## Getting Started

### Prerequisites

- Python 3.x
- `pytest` for running tests

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/mezzzies/ToyRobot.git

Install the required packages:
$pip install pytest

## How to Run

You can run the simulator by entering commands interactively.

### Running Interactively

Run the simulator without any arguments to enter commands interactively:

```sh
python ToyRobot.py
```

Enter commands one by one:

```
PLACE 0,0,NORTH
MOVE
REPORT
```

## Commands

- `PLACE X,Y,F`: Place the robot at position (X,Y) facing direction F (NORTH, EAST, SOUTH, WEST).
- `MOVE`: Move the robot one unit forward in the direction it is currently facing.
- `LEFT`: Rotate the robot 90 degrees to the left.
- `RIGHT`: Rotate the robot 90 degrees to the right.
- `REPORT`: Print the current position and direction of the robot.

## Running Tests

To run the tests, use `pytest` or `python -m pytest test_ToyRobot.py`:

```sh
pytest test_ToyRobot.py
```
