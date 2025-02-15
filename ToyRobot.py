class Table:
    def __init__(self, table_size):
        self.table_size = table_size

class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.placed = False

    def place(self, x, y, facing,table_size):
        try:
            x, y = float(x), float(y)
            if not x.is_integer() or not y.is_integer():
                print("Invalid x or y: floating point not allowed")
                return
            else:
                x, y = int(x), int(y)
                if 0 <= x <= table_size and 0 <= y <= table_size and facing in self.directions:
                    self.x = x
                    self.y = y
                    self.facing = facing
                    self.placed = True
                else:
                    print("Invalid x or y or facing")
        except ValueError:
            print("Invalid x or y: integer expected")

    def move(self,table_size):
        if self.x is None or self.y is None:
            return
        
        if self.facing == "NORTH" and self.y < table_size:
            self.y += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "EAST" and self.x < table_size:
            self.x += 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1
        else:
            if self.x == 0 and self.facing == "WEST":
                print("Robot is at the western edge")
            elif self.x == table_size and self.facing == "EAST":
                print("Robot is at the eastern edge")
            elif self.y == 0 and self.facing == "SOUTH":
                print("Robot is at the southern edge")
            elif self.y == table_size and self.facing == "NORTH":
                print("Robot is at the northern edge")
            else:
                print("Invalid move")

    def left(self):
        if self.facing:
            self.facing = self.directions[(self.directions.index(self.facing) - 1) % 4]

    def right(self):
        if self.facing:
            self.facing = self.directions[(self.directions.index(self.facing) + 1) % 4]

    def report(self):
        if self.placed:
            report_string = str(self.x) + "," + str(self.y) + "," + str(self.facing)
            return report_string

# DEBUG
# def print_status(robot):
#     print(f"----x = {robot.x}")
#     print(f"    y = {robot.y}")
#     print(f"    face = {robot.facing}")

def process_command(robot,table,text):
    parts = text.split(" ",1)
    command = parts[0]

    if command == "PLACE" and len(parts) == 2:
        values = parts[1].split(",")  # Split the second part by ","
        if len(values) == 3:
            x,y,face = values
            robot.place(x,y,face,table.table_size)
            #print_status(robot)
        else:
            print("Invalid format. Expected: PLACE x,y,face")
        
    elif command == "MOVE":
        if robot.placed:
            robot.move(table.table_size)
            #print_status(robot)
        else:
            print("Robot is not placed yet")
    
    elif command == "LEFT":
        if robot.placed:
            robot.left()
            #print_status(robot)
        else:
            print("Robot is not placed yet")
    elif command == "RIGHT":
        if robot.placed:
            robot.right()
            #print_status(robot)
        else:
            print("Robot is not placed yet")
    elif command == "REPORT":
        if robot.placed:
            print(robot.report())
        else:
            print("Robot is not placed yet")
    else:
        print("Valid commands are: PLACE X,Y,F | MOVE | LEFT | RIGHT | REPORT")

def main():
    try:
        robot = Robot()
        table = Table(5)
        print("Hi! Welcome to Toy Robot")
        print("Valid commands are: PLACE X,Y,Face | MOVE | LEFT | RIGHT | REPORT")
        print("Note: Place the robot first, Face = [NORTH,EAST,WEST,SOUTH]")
        print("Enter the input or Ctrl+C to exit ...")
        while True:
            line = input().strip()
            process_command(robot,table,line)
    except EOFError:
        pass  # Handle end of input gracefully
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
