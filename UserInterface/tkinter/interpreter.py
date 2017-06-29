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
            return ['y', 2, 0, 0]
    
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
            return ['y', 1, 0, 0]

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
                    return ['y', 0, 1, 0]
                else:
                    return ['y', 0, 2, 0]
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
            return ['y', 0, 0, degrees]
        '''degrees = 90
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
                text_box.configure(state="disabled")'''

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

    return ['n', 0, 0, 0]
