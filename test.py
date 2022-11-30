from tkinter import *
from tkinter.ttk import Notebook


class MyFrame1(Frame):
    def __init__(self, master=None, mytext=""):
        super().__init__(master)
        self.create_widgets(mytext)

    def create_widgets(self, mytext):
        self.label = Label(self.master, text=mytext, anchor=W)
        # this is not placed relative to the Frame, but to the
        # master
        # 1. How I get the relative coordinates inside the frame
        #    to be 10, 10 of the frame area?
        self.label.place(x=10, y=10, width=128, height=24)


class MyNotebook(Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.f1 = MyFrame1(self, "abc")
        # once the UI is drawn, the label "def" seems to overlay
        # "abc" even when "f1" is selected
        # 2. Why is self.f2 always shown even when self.f1 is
        #    selected?
        self.f2 = MyFrame1(self, "def")
        self.add(self.f1, text="f1")
        self.add(self.f2, text="f2")
        # Without this command nothing gets drawn
        # 3. Why is this? Is this equivalent of 'pack' but for
        #    pixel driven layout?
        self.place(width=640, height=480)


def main():
    root = Tk()
    root.minsize(640, 480)
    root.geometry("640x480")
    app = MyNotebook(master=root)
    # this works as intended the label is indeed placed
    # in the frame at 10, 10
    # app = MyFrame1(master=root, mytext="123abc")
    app.mainloop()
    return None


if __name__ == "__main__":
    main()
