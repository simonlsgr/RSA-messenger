import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import functools


window_height = 550
window_width = 800


# Frame in whin is the chat
class ChatFrame(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#28192e", border_color="#3e325d", border_width=1, corner_radius=0, width=800-260)

    def create_widgets(self):
        pass


# Frame in which is the chat list
class Conversation_List(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#1f192e", border_color="#3e325d", border_width=2, corner_radius=0, width=260)

    def func(name):
        print(name)

    def create_widgets(self):
        self.conversation_header = ctk.CTkLabel(self, text="Conversation_Buttons", text_font=("Arial", 16, "bold"))
        self.conversation_header.pack(side="top", fill="x", pady=5, padx=10)

        self.canvas_container = Canvas(self, height=100)
        self.frame2 = ctk.CTkFrame(self)
        #self.scrollbar = ttk.Scrollbar(self.frame2, orient="vertical", command=self.canvas_container.yview)
        #self.scrollbar.pack(side="right", fill=Y)
        self.canvas_container.create_window((0, 0), window=self.frame2, anchor='nw')

        self.mylist = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9']
        for item in self.mylist:
            self.button = ttk.Button(self.frame2, text=item)
            self.button.pack()


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
