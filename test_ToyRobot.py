import pytest
from ToyRobot import Robot

def test_place_robot():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.facing == "NORTH"

def test_move_robot():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.move()
    assert robot.x == 0
    assert robot.y == 1

def test_turn_left():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.left()
    assert robot.facing == "WEST"

def test_turn_right():
    robot = Robot()
    robot.place(0, 0, "NORTH")
    robot.right()
    assert robot.facing == "EAST"

def test_report():
    robot = Robot()
    robot.place(0, 0, "EAST")
    assert robot.report() == "0,0,EAST"

def test_invalid_place():
    robot = Robot()
    robot.place(6, 6, "NORTH")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_move_out_of_bounds():
    robot = Robot()
    robot.place(0, 0, "SOUTH")
    robot.move()
    assert robot.y == 0

    robot.place(0, 0, "WEST")
    robot.move()
    assert robot.x == 0

    robot.place(5, 5, "NORTH")
    robot.move()
    assert robot.y == 5

    robot.place(5, 5, "EAST")
    robot.move()
    assert robot.x == 5

def test_place_invalid_facing():
    robot = Robot()
    robot.place(0, 0, "UP")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_move_without_place():
    robot = Robot()
    robot.move()
    assert robot.x is None
    assert robot.y is None

def test_turn_left_without_place():
    robot = Robot()
    robot.left()
    assert robot.facing is None

def test_turn_right_without_place():
    robot = Robot()
    robot.right()
    assert robot.facing is None

def test_report_without_place():
    robot = Robot()
    assert robot.report() is None
