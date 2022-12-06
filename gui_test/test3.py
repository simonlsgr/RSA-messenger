from tkinter import *


class ScrolledCanvas():
    def __init__(self, parent, color='brown'):
        canv = Canvas(parent, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)

        ##---------- scrollregion has to be larger than canvas size
        ##           otherwise it just stays in the visible canvas
        canv.config(scrollregion=(0, 0, 300, 1000))
        canv.config(highlightthickness=0)

        ybar = Scrollbar(parent)
        ybar.config(command=canv.yview)
        ## connect the two widgets together
        canv.config(yscrollcommand=ybar.set)
        ybar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for ctr in range(10):
            frm = Frame(parent, width=960, height=100, bg="#cfcfcf", bd=2)
            frm.config(relief=SUNKEN)
            Label(frm, text="Frame #" + str(ctr + 1)).grid()
            canv.create_window(10, 10 + (100 * ctr), anchor=NW, window=frm)


if __name__ == '__main__':
    root = Tk()
    ScrolledCanvas(root)
    root.mainloop()