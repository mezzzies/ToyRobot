# Toy Robot Simulator

This is a simple toy robot simulator. The robot can be placed on a 5x5 table, moved around, and report its position and facing direction. The project includes a main script `ToyRobot.py` and a test script `test_ToyRobot.py` using `pytest`.

## Usage Time

- **Design**: 0.25 MH
- **Implementation**: 1-1.5 MH
- **Testing**: 0.5 MH
- **Revision**: 0.5 MH

## Getting Started

### Prerequisites

- Python 3.x
- `pytest` for running tests

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/mezzzies/ToyRobot.git
   ```

2. Install the required packages:
   ```sh
   pip install pytest
   ```

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
RIGHT
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

```
=================== test session starts ====================
platform win32 -- Python 3.11.9, pytest-8.3.4, pluggy-1.5.0
rootdir: D:\01_Working\06_Programming\Toy_Robot
collected 25 items

test_ToyRobot.py .........................            [100%]

==================== 25 passed in 0.05s ====================
```
