import math
import turtle
from interface import interface

line_number=1

def interpret(program,turt,text_box,command,code_box):
    command = command.lower()
    command_array = command.split()

    backward_array = ["backwards", "back", "backward"]
    forward_array  = ["forward", "go", "forwards", "move"]
    rotate_array   = ["rotate", "turn", "degrees"]
    face_array     = ["face", "up", "down", "left", "right", "east", "west", "north", "south"]
    circle_array   = ["circle","radius","diameter"]

    # Moving backward
    if any(i in backward_array for i in command_array):
        return backward(command_array,text_box,code_box,turt)
    
    # Moving forward
    elif any(i in forward_array for i in command_array):
        return forward(command_array,text_box,code_box,turt)

    # Turn a certain number of degrees
    elif any(i in rotate_array for i in command_array):
        return rotate(command_array,text_box,code_box,turt)
        
    # Face a certain direction
    elif any(i in face_array for i in command_array):
        return face(command_array,text_box,code_box,turt)

    # Make a circle with a certain radius or diameter
    elif any(i in circle_array for i in command_array):
        return circle(command_array,text_box,code_box,turt)

    # Clear the screen
    elif "clear" in command_array:
        text_box.configure(state="normal")
        text_box.insert("end","Okay! Clearing the screen!\n")
        text_box.configure(state="disabled")
        turt.clear()
        turt.penup()
        turt.home()
        turt.pendown()

    # Quit the program
    elif "quit" in command_array:
        program.quit()
        
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Sorry, I didn't understand that.\nCould you rephrase that?\n")
        text_box.configure(state="disabled")

    return ['n', 0, 0, 0, 0,0]

def border_movement(turt, command, num_steps):
    turt_x = turt.xcor()
    turt_y = turt.ycor()
    turt_angle = turt.heading()
    if command != "circle":
        if command == "backwards":
            if turt_angle < 180:
                turt_angle += 180
            else:
                turt_angle -= 180
        new_x = turt_x + (math.cos(math.radians(turt_angle)) * num_steps)
        new_y = turt_y + (math.sin(math.radians(turt_angle)) * num_steps)
        if math.fabs(new_x) <= 300 and math.fabs(new_y) <= 300:
            if command == "backwards":
                turt.back(num_steps)
            elif command == "forwards":
                turt.fd(num_steps)
        elif math.fabs(new_x) > 300 and math.fabs(new_y) < 300:
            print("Too far (x-axis)")
            new_steps=(num_steps*(300-math.fabs(turt_x)))/(math.fabs(new_x)-math.fabs(turt_x))
            if command=="backwards":
                turt.back(new_steps)
            elif command=="forwards":
                turt.fd(new_steps)
        elif math.fabs(new_y) > 300 and math.fabs(new_x) < 300:
            print("Too far (y-axis)")
            new_steps=(num_steps*(300-math.fabs(turt_y)))/(math.fabs(new_y)-math.fabs(turt_y))
            if command=="backwards":
                turt.back(new_steps)
            elif command=="forwards":
                turt.fd(new_steps)
        else:
            print("Too far!!!!")    

# Move backwards
def backward(command_array,text_box,code_box,turt):
    steps = 0;
    global line_number;
    for item in command_array:
        if item.isdigit():
            steps = int(item)
            break
    if steps > 0:
        text_box.configure(state="normal")
        text_box.insert("end","Okay! Moving backward %d steps!\n" % steps)
        text_box.configure(state="disabled")
        code_box.configure(state="normal")
        code_box.insert("end","%d: back(%d)\n" % (line_number,steps))
        code_box.configure(state="disabled")
        line_number = line_number + 1
        border_movement(turt, "backwards", steps)
        #turt.backward(steps)
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Please enter a valid number\nof steps to move backward.\n")
        text_box.configure(state="disabled")
        return ['y', 2, 0, 0, 0, 0]
    return ['n', 0, 0, 0, 0, 0]

# Move forward
def forward(command_array,text_box,code_box,turt):
    steps = 0
    global line_number
    for item in command_array:
        if item.isdigit():
            steps = int(item)
            break
    if steps > 0:
        text_box.configure(state="normal")
        text_box.insert("end","Okay! Moving forward %d steps!\n" % steps)
        text_box.configure(state="disabled")
        code_box.configure(state="normal")
        code_box.insert("end","%d: fd(%d)\n" % (line_number,steps))
        code_box.configure(state="disabled")
        line_number = line_number + 1
        border_movement(turt, "forwards", steps)
        #turt.fd(steps)
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Please enter a valid number\nof steps to move forward.\n")
        text_box.configure(state="disabled")
        return ['y', 1, 0, 0, 0, 0]
    return ['n', 0, 0, 0, 0, 0]

# Rotate
def rotate(command_array,text_box,code_box,turt):
    degrees = -1
    global line_number
    for item in command_array:
        if item.isdigit():
            degrees=int(item)
            break
    if "right" in command_array or "left" in command_array:
        if degrees <= -1:
            text_box.configure(state="normal")
            text_box.insert("end","How many degrees would you\nlike the turtle to turn?\n")
            text_box.configure(state="disabled")
            if "right" in command_array:
                return ['y', 0, 1, 0, 0, 0]
            else:
                return ['y', 0, 2, 0, 0, 0]
        else:
            if "right" in command_array:
                text_box.configure(state="normal")
                text_box.insert("end","Okay! Turning right %d degrees!\n" % degrees)
                text_box.configure(state="disabled")
                code_box.configure(state="normal")
                code_box.insert("end","%d: right(%d)\n" % (line_number, degrees))
                code_box.configure(state="disabled")
                turt.right(degrees)
            else:
                text_box.configure(state="normal")
                text_box.insert("end","Okay! Turning left %d degrees!\n" % degrees)
                text_box.configure(state="disabled")
                code_box.configure(state="normal")
                code_box.insert("end","%d: left(%d)\n" % (line_number, degrees))
                code_box.configure(state="disabled")
                turt.left(degrees)
            line_number = line_number + 1
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Would you like the turtle to turn\nto the right or left?\n")
        text_box.configure(state="disabled")
        return ['y', 0, 0, degrees, 0,0]
    return ['n', 0, 0, 0, 0,0]
    
def face(command_array,text_box,code_box,turt):
     global line_number
     if "left" in command_array or "west" in command_array:
         text_box.configure(state="normal")
         text_box.insert("end","Okay! Turning to the west!\n")
         text_box.configure(state="disabled")
         code_box.configure(state="normal")
         code_box.insert("end","%d: setheading(180)\n" % line_number)
         code_box.configure(state="disabled")
         turt.setheading(180)
     elif "up" in command_array or "north" in command_array:
         text_box.configure(state="normal")
         text_box.insert("end","Okay! Turning to the north!\n")
         text_box.configure(state="disabled")
         code_box.configure(state="normal")
         code_box.insert("end","%d: setheading(90)\n" % line_number)
         code_box.configure(state="disabled")
         turt.setheading(90)
     elif "right" in command_array or "east" in command_array:
         text_box.configure(state="normal")
         text_box.insert("end","Okay! Turning to the east!\n")
         text_box.configure(state="disabled")
         code_box.configure(state="normal")
         code_box.insert("end","%d: setheading(0)\n" % line_number)
         code_box.configure(state="disabled")
         turt.setheading(0)
     elif "down" in command_array or "south" in command_array:
         text_box.configure(state="normal")
         text_box.insert("end","Okay! Turning to the south!\n")
         text_box.configure(state="disabled")
         code_box.configure(state="disabled")
         code_box.insert("end","%d: setheading(270)\n" % line_number)
         turt.setheading(270)
     else:
         text_box.configure(state="normal")
         text_box.insert("end","What direction would you like\nthe turtle to face?\n")
         text_box.configure(state="disabled")
         return ['y', 0, 0, 0, 1,0]
     line_number = line_number + 1
     return ['n',0,0,0,0,0]

def circle(command_array,text_box,code_box,turt):
    global line_number
    num = 0
    for item in command_array:
        if item.isdigit():
            num = int(item)
            break
    if num <= 0:
        if "radius" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","What would you like the radius\nto be?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, 0, 0, -1,0]
        if "diameter" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","What would you like the\ndiameter to be?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, 0, 0, -2]
        else:
            text_box.configure(state="normal")
            text_box.insert("end","How large would you like the\ncircle to be?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, 0, 0, -3]
    else:
        if "radius" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Making a circle of\nradius %d!\n" % num)
            text_box.configure(state="disabled")
            code_box.configure(state="normal")
            code_box.insert("end","%d: circle(%d)\n" % (line_number,num))
            code_box.configure(state="disabled")
            turt.circle(num)
        elif "diameter" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Making a circle of\ndiameter %d!\n" % num)
            text_box.configure(state="disabled")
            code_box.configure(state="normal")
            code_box.insert("end","%d: circle(%d)\n" % (line_number,num/2))
            code_box.configure(state="disabled")
            turt.circle(num/2)
        else:
            text_box.configure(state="normal")
            text_box.insert("end","Is the number provided the\ncircle's radius or diameter?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, 0, 0, num]
        line_number=line_number+1
    return ['n',0,0,0,0,0]
