class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.table_size = 5
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        self.placed = False

    def place(self, x, y, facing):
        try:
            x, y = int(x), int(y)
            if 0 <= x <= self.table_size and 0 <= y <= self.table_size and facing in self.directions:
                self.x = x
                self.y = y
                self.facing = facing
                self.placed = True
        except ValueError:
            print("Invalid x or y")

    def move(self):
        if self.x is None or self.y is None:
            return
        
        if self.facing == "NORTH" and self.y < self.table_size:
            self.y += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "EAST" and self.x < self.table_size:
            self.x += 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1

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

def process_command(robot,text):
    parts = text.split(" ",1)
    command = parts[0]

    if command == "PLACE" and len(parts) == 2:
        values = parts[1].split(",")  # Split the second part by ","
        if len(values) == 3:
            x,y,face = values
            robot.place(x,y,face)
            #print_status(robot)
            robot.placed = True
        else:
            print("Invalid format. Expected: PLACE x,y,face")
        
    elif command == "MOVE":
        if robot.placed:
            robot.move()
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
        print("Hi! Welcome to Toy Robot")
        print("Valid commands are: PLACE X,Y,Face | MOVE | LEFT | RIGHT | REPORT")
        print("Note: Place the robot first, Face = [NORTH,EAST,WEST,SOUTH]")
        print("Enter the input or Ctrl+C to exit ...")
        while True:
            line = input().strip()
            process_command(robot,line)
    except EOFError:
        pass  # Handle end of input gracefully
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
