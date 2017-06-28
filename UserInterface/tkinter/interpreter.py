import turtle
from interface import interface

def interpret(turt,text_box,command):
    command = command.lower()
    command_array = command.split()

    # Moving backward
    if "backward" in command_array or "backwards" in command_array:
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
    
    # Moving forward
    elif "go" in command_array or "forward" in command_array or "forwards" in command_array:
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

    # Turn a certain number of degrees
    elif "turn" in command_array:
        degrees = 90
        for item in command_array:
            if item.isdigit():
                degrees = int(item)
                break
        for item in command_array:
            if item == "right":
                turt.right(degrees)
                text_box.configure(state="normal")
                text_box.insert("end","Okay! Turning right %d degrees!\n" % degrees)
                text_box.configure(state="disabled")
            if item == "left":
                turt.left(degrees)
                text_box.configure(state="normal")
                text_box.insert("end","Okay! Turning left %d degrees!\n" % degrees)
                text_box.configure(state="disabled")

    elif "clear" in command_array:
        text_box.configure(state="normal")
        text_box.insert("end","Okay! Clearing the screen!\n")
        text_box.configure(state="disabled")
        turt.clear()
        turt.penup()
        turt.home()
        turt.pendown()
        
    else:
        text_box.configure(state="normal")
        text_box.insert("end","Sorry, I didn't understand that.\nCould you rephrase that?\n")
        text_box.configure(state="disabled")
