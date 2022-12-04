import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functools

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
        self.frame_container = ctk.CTkFrame(self)

        self.conversation_header = ctk.CTkLabel(self, text="Conversation_Buttons", text_font=("Arial", 16, "bold"), width=260)
        self.conversation_header.pack(side="top", fill="x", pady=6, padx=10, anchor="n")

        self.canvas_container = ctk.CTkCanvas(self.frame_container, height=500, bg="#1f192e")
        self.frame2 = ctk.CTkFrame(self.canvas_container, bg="#1f192e", border_width=0, width=260, height=800)
        self.frame2.configure(fg_color="#1f192e")
        self.myscrollbar = ttk.Scrollbar(self.frame_container, orient="vertical",
                                command=self.canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        self.canvas_container.create_window((0, 0), window=self.frame2, anchor='nw')

        def func(name):
            print(name)

        self.mylist = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10', 'item11']
        for item in self.mylist:
            self.button = ctk.CTkButton(self.frame2, text=item, command=functools.partial(func, item),
                                        width=200, height=50, corner_radius=5, border_width=2)
            self.button.pack(pady=3, padx=3)
            print(item)

        self.frame2.update()  # update frame2 height, so it's no longer 0 ( height is 0 when it has just been created )
        self.frame_container.update()  # update frame_container height, so it's no longer 0 ( height is 0 when it has just been created )
        self.canvas_container.configure(yscrollcommand=self.myscrollbar.set)  # the scrollregion mustbe the size of the frame inside it,
        # in this case "x=0 y=0 width=0 height=frame2height"
        # width 0 because we only scroll verticaly so don't mind about the width.

        self.canvas_container.config(scrollregion=(0, 0, 0, 1000))
        self.canvas_container.configure(background="#1f192e")

        self.frame2.pack(fill=tk.BOTH, expand=False)
        self.canvas_container.pack(side=tk.LEFT)
        self.myscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.myscrollbar.configure(command=self.canvas_container.yview)
        self.myscrollbar.update()
        self.frame2.update()
        self.frame_container.pack()

        pass


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
