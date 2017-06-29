import turtle
from interface import interface

def interpret(program,turt,text_box,command):
    command = command.lower()
    command_array = command.split()

    # Moving backward
    if "backward" in command_array or "backwards" in command_array or "back" in command_array:
        steps = 0;
        for item in command_array:
            if item.isdigit():
                steps = int(item)
                break
        if steps != 0:
            turt.backward(steps)
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Moving backward %d steps!\n" % steps)
            text_box.configure(state="disabled")
        else:
            text_box.configure(state="normal")
            text_box.insert("end","Please enter a valid number\nof steps to move backward.\n")
            text_box.configure(state="disabled")
            return ['y', 2, 0, 0, 0]
    
    # Moving forward
    elif "go" in command_array or "forward" in command_array or "forwards" in command_array or "move" in command_array:
        steps = 0
        for item in command_array:
            if item.isdigit():
                steps = int(item)
                break
        if steps != 0:
            turt.fd(steps)
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Moving forward %d steps!\n" % steps)
            text_box.configure(state="disabled")
        else:
            text_box.configure(state="normal")
            text_box.insert("end","Please enter a valid number\nof steps to move forward.\n")
            text_box.configure(state="disabled")
            return ['y', 1, 0, 0, 0]

    # Turn a certain number of degrees
    elif "rotate" in command_array or "turn" in command_array or "degrees" in command_array:
        degrees = -1
        for item in command_array:
            if item.isdigit():
                degrees=int(item)
                break
        if "right" in command_array or "left" in command_array:
            if degrees == -1:
                text_box.configure(state="normal")
                text_box.insert("end","How many degrees would you\nlike the turtle to turn?\n")
                text_box.configure(state="disabled")
                if "right" in command_array:
                    return ['y', 0, 1, 0, 0]
                else:
                    return ['y', 0, 2, 0, 0]
            else:
                if "right" in command_array:
                    text_box.configure(state="normal")
                    text_box.insert("end","Okay! Turning right %d degrees!\n" % degrees)
                    text_box.configure(state="disabled")
                    turt.right(degrees)
                else:
                    text_box.configure(state="normal")
                    text_box.insert("end","Okay! Turning left %d degrees!\n" % degrees)
                    text_box.configure(state="disabled")
                    turt.left(degrees)
        else:
            text_box.configure(state="normal")
            text_box.insert("end","Would you like the turtle to turn\nto the right or left?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, degrees, 0]

    # Face a certain direction
    elif any(i in ['face','left','right','up','down','north','south','east','west'] for i in command_array):
        if "left" in command_array or "west" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Turning to the west!\n")
            text_box.configure(state="disabled")
            turt.setheading(180)
        elif "up" in command_array or "north" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Turning to the north!\n")
            text_box.configure(state="disabled")
            turt.setheading(90)
        elif "right" in command_array or "east" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Turning to the east!\n")
            text_box.configure(state="disabled")
            turt.setheading(0)
        elif "down" in command_array or "south" in command_array:
            text_box.configure(state="normal")
            text_box.insert("end","Okay! Turning to the south!\n")
            text_box.configure(state="disabled")
            turt.setheading(270)
        else:
            text_box.configure(state="normal")
            text_box.insert("end","What direction would you like\nthe turtle to face?\n")
            text_box.configure(state="disabled")
            return ['y', 0, 0, 0, 1]

    # Clear the screen
    elif "clear" in command_array:
        text_box.configure(state="normal")
        text_box.insert("end","Okay! Clearing the screen!\n")
        text_box.configure(state="disabled")
        turt.clear()
        turt.penup()
        turt.home()
        turt.pendown()

    elif "quit" in command_array:
        program.quit()
        
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Sorry, I didn't understand that.\nCould you rephrase that?\n")
        text_box.configure(state="disabled")

    return ['n', 0, 0, 0, 0]
