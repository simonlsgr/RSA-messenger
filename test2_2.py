import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

window_height = 550
window_width = 800


# Frame in which is the chat
class ChatFrame(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#28192e",
                       border_color="#3e325d",
                       border_width=1,
                       corner_radius=0,
                       width=800 - 260)

    def create_widgets(self):
        pass


# Frame in which is the chat list
class Conversation_List(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#1f192e",
                       border_color="#3e325d",
                       border_width=2,
                       corner_radius=0,
                       width=260)

    def create_widgets(self):
        conversation_header = ctk.CTkLabel(self, text="Conversations", text_font=("Arial", 16, "bold"), width=260)
        conversation_header.pack(side="top", fill="x", pady=6, padx=10, anchor="n")
        Conversation_Buttons(self)


class Conversation_Buttons():
    def __init__(self, parent, color="#1f192e"):

        canv = ctk.CTkCanvas(parent, bg=color)
        canv.config(width=300, height=200)

        # scrollregion has to be larger than canvas size
        # otherwise it just stays in the visible canvas
        canv.config(scrollregion=(0, 0, 300, 1000))
        canv.config(highlightthickness=0)

        ybar = ttk.Scrollbar(parent)
        ybar.config(command=canv.yview)
        # connect the two widgets together
        canv.config(yscrollcommand=ybar.set)
        ybar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for ctr in range(40):
            """frm = ctk.CTkFrame(parent, width=960, height=100, bd=2, bg_color="#1f192e")
            frm.config(relief=SUNKEN)
            ctk.CTkLabel(frm, text="Frame #" + str(ctr + 1)).grid()
            canv.create_window(10, 10 + (100 * ctr), anchor=NW, window=frm)
            
            # btn_frm.config(relief=SUNKEN)
            ctk.CTkButton(btn_frm, text="Button #" + str(ctr + 1)).grid()
            """
            btn_frm = ctk.CTkFrame(canv, width=960, height=100, fg_color="#1f192e")
            ctk.CTkButton(btn_frm, text="Button #" + str(ctr + 1), width=230, height=50, corner_radius=5,
                          border_width=2).grid()
            canv.create_window(10, 3 + (62 * ctr), anchor=NW, window=btn_frm)


# Class for main Window
class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Messenger")
        self.geometry("800x550+310+100")
        self.resizable(False, False)
        self.configure(bg="#28192e")
        self.create_widgets()

    def create_widgets(self):
        chat_window = ChatFrame(self)
        chat_window.pack(side="right", fill=tk.BOTH, expand=False)

        conversation_list = Conversation_List(self)
        conversation_list.pack(side="left", fill=tk.BOTH, expand=False)


if __name__ == "__main__":
    app = Main_Window()
    app.mainloop()
