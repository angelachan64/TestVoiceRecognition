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
        text_input.bind("<Return>",(lambda event: command_entry(text_input.get())))
        text_input.pack(side=LEFT)
        text_input.focus()
        button_enter = Button(frame5, text="Submit", width=7, command=lambda:command_entry(text_input.get()))
        button_enter.pack(side=RIGHT)

        def command_entry(command):
            text_box.configure(state="normal")
            text_box.insert("end", "%s\n" % command, 'tag-right')
            text_box.configure(state="disabled")
            interpreter.interpret(turt,text_box,command)
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
