try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
except ImportError:
    from tkinter.ttk import *
import turtle
import interpreter

yn_repeat=['n',0,0,0]
# repeat, move, turn
class interface(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("PiE LOGO")
        self.pack(fill=BOTH, expand=1)
        self.center()

        # Top heading bar
        frame1 = Frame(self)
        frame1.pack(fill=X)
        label_1 = Label(frame1, text="Welcome!", width = 9)
        label_1.pack(side=LEFT, padx = 5, pady = 5)
        button_quit = Button(frame1, text="Quit", command=self.quit)
        button_quit.pack(side = RIGHT, padx = 5, pady = 5)

        # LOGO canvas
        frame2 = Frame(self)
        frame2.pack(side=LEFT, fill=X)
        canv = Canvas(frame2, width=600, height=600)
        canv.pack(side=LEFT, padx=5, pady=5)
        turt = turtle.RawTurtle(canv)
        screen = turt.getscreen()
        turt.shape("turtle")

        # Text and Entry
        frame3 = Frame(self)
        frame3.pack(side=RIGHT, fill=Y)

        # Display past commands
        frame4 = Frame(frame3)
        frame4.pack(side=TOP, fill=X)
        text_box = Text(frame4, height=35, width=33, state="disabled")
        text_box.pack(side=LEFT)
        text_box.tag_configure('tag-right', justify='right')
        scroll_bar = Scrollbar(frame4)
        scroll_bar.pack(side=RIGHT, fill=Y)
        scroll_bar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar.set)

        text_box.configure(state="normal")
        text_box.insert("end","Hello! Welcome to PiE LOGO!\n")
        text_box.insert("end","Please type in a command and\nthe turtle on the screen will\nfollow your instructions.\n")
        text_box.insert("end","Please input one command at\na time!\n")
        text_box.configure(state="disabled")

        # Command entry
        frame5 = Frame(frame3)
        frame5.pack(side=BOTTOM, fill=X)
        text_input = Entry(frame5, width=33)
        text_input.bind("<Return>",(lambda event: self.command_entry(text_box,text_input,turt,yn_repeat,text_input.get())))
        text_input.pack(side=LEFT)
        text_input.focus()
        button_enter = Button(frame5, text="Submit", width=7, command=lambda:self.command_entry(text_box,text_input,turt,yn_repeat,text_input.get()))
        button_enter.pack(side=RIGHT)

    def command_entry(self,text_box,text_input,turt,yn_repeat1,command):
        global yn_repeat
        #print(yn_repeat)
        if len(command.split()) != 0:
            text_box.configure(state="normal")
            text_box.insert("end", "%s\n" % command, 'tag-right')
            text_box.configure(state="disabled")
            if yn_repeat1[0]=='y':
                command.lower()
                command_array = command.split()
                num = 0
                for item in command_array:
                    if item.isdigit():
                        num = int(item)
                for item in yn_repeat1[1:]:
                    if item != 0:
                        if yn_repeat1.index(item) == 1:
                            if item == 1:
                                yn_repeat = interpreter.interpret(self,turt,text_box,"forward %d" % num)
                            elif item == 2:
                                yn_repeat = interpreter.interpret(self,turt,text_box,"backward %d" % num)
                        elif yn_repeat1.index(item)==2:
                            if item==1:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"turn right %d" % num)
                            elif item==2:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"turn left %d" % num)
                        elif yn_repeat1.index(item)==3:
                            if "right" in command_array:
                                if item != -1:
                                    yn_repeat=interpreter.interpret(self,turt,text_box,"turn right %d" % item)
                                else:
                                    yn_repeat=interpreter.interpret(self,turt,text_box,"turn right")
                            elif "left" in command_array:
                                if item != -1:
                                    yn_repeat=interpreter.interpret(self,turt,text_box,"turn left %d" % item)
                                else:
                                    yn_repeat=interpreter.interpret(self,turt,text_box,"turn left")
                        elif yn_repeat1.index(item)==4:
                            if "right" in command_array or "east" in command_array:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"east")
                            elif "left" in command_array or "west" in command_array:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"west")
                            elif "up" in command_array or "north" in command_array:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"north")
                            elif "down" in command_array or "south" in command_array:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"south")
                            else:
                                yn_repeat=interpreter.interpret(self,turt,text_box,"face")
                            
            else:
                yn_repeat = interpreter.interpret(self,turt,text_box,command)
        text_input.delete(0,'end')
        text_input.focus()
            

    def center(self):
        w = 900
        h = 620
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2 - 25
        self.parent.geometry("%dx%d+%d+%d" % (w, h, x, y))

def main():
    root = Tk()
    app = interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
