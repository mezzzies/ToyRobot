import pytest
from ToyRobot import Table,Robot,process_command

#Unit test cases
#Positive test cases
#Fix table_size to 5
def test_place_robot():
    robot = Robot()
    robot.place(0, 0, "NORTH",5)
    assert robot.x == 0
    assert robot.y == 0
    assert robot.facing == "NORTH"

def test_move_robot():
    robot = Robot()
    robot.place(0, 0, "NORTH",5)
    robot.move(5)
    assert robot.x == 0
    assert robot.y == 1

def test_turn_left():
    robot = Robot()
    robot.place(0, 0, "NORTH",5)
    robot.left()
    assert robot.facing == "WEST"

def test_turn_right():
    robot = Robot()
    robot.place(0, 0, "NORTH",5)
    robot.right()
    assert robot.facing == "EAST"

def test_report():
    robot = Robot()
    robot.place(0, 0, "EAST",5)
    assert robot.report() == "0,0,EAST"

#Negative test cases

def test_exceed_place():
    robot = Robot()
    robot.place(6, 6, "NORTH",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_float_place():
    robot = Robot()
    robot.place(1.4, 1.6, "EAST",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_negative_place():
    robot = Robot()
    robot.place(-1, -1, "EAST",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_not_int_xy_place():
    robot = Robot()
    robot.place("x", "y", "EAST",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_move_out_of_bounds():
    robot = Robot()
    robot.place(0, 0, "SOUTH",5)
    robot.move(5)
    assert robot.y == 0

    robot.place(0, 0, "WEST",5)
    robot.move(5)
    assert robot.x == 0

    robot.place(5, 5, "NORTH",5)
    robot.move(5)
    assert robot.y == 5

    robot.place(5, 5, "EAST",5)
    robot.move(5)
    assert robot.x == 5

def test_place_invalid_facing():
    robot = Robot()
    robot.place(0, 0, "UP",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_place_space_facing():
    robot = Robot()
    robot.place(0, 0, " NORTH",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

    robot.place(0, 0, "NORTH ",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

    robot.place(0, 0, "NO RTH",5)
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_move_without_place():
    robot = Robot()
    robot.move(5)
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

#Integration test cases
def test_int_place_robot():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,0,EAST")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.facing == "EAST"

def test_int_move_robot():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,0,EAST")
    process_command(robot,table,"MOVE")
    assert robot.x == 1
    assert robot.y == 0
    assert robot.facing == "EAST"

def test_int_turn_robot():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,0,EAST")
    process_command(robot,table,"LEFT")
    assert robot.x == 0
    assert robot.y == 0
    assert robot.facing == "NORTH"

def test_int_report_robot():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,0,EAST")
    process_command(robot,table,"REPORT")
    assert robot.report() == "0,0,EAST"

#Negative test cases
def test_place_exceeded_param():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,0,EAST,1")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_place_less_param():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"PLACE 0,EAST")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

    process_command(robot,table,"PLACE 0,0")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

    process_command(robot,table,"PLACE EAST")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_invalid_place_then_move():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"0, -1, EAST")
    process_command(robot,table,"MOVE")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None

def test_invalid_place_then_turn():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"0, -1, EAST")
    process_command(robot,table,"LEFT")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None
    
def test_invalid_place_then_report():
    robot = Robot()
    table = Table(5)
    process_command(robot,table,"0, -1, EAST")
    process_command(robot,table,"REPORT")
    assert robot.x is None
    assert robot.y is None
    assert robot.facing is None