import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Test")
        self.geometry("400x400")
        self.resizable(False, False)
        self.configure(bg="#000000")
        self.create_widgets()

    def create_widgets(self):
        # create chat window

        self.chat_window = tk.Text(self, bg="#000000", fg="#FFFFFF",
                                   font=("Arial", 12), width=20, height=2, padx=5, pady=5)
        self.chat_window.grid(row=0, column=0, padx=5, pady=5)

        self.btn = ttk.Button(self, text="Test", command=self.btn_click)
        self.btn.grid(row=1, column=0, padx=5, pady=5)

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(master=self, corner_radius=6)
        button.grid(row=0, column=1, padx=10, pady=10)

        entry = ctk.CTkTextbox(master=self,
                               width=120,
                               height=50,
                               corner_radius=10)
        entry.grid(row=1, column=1, padx=10, pady=10)

        label = ctk.CTkLabel(master=self,
                             text="CTkLabel",
                             width=120,
                             height=25,
                             corner_radius=10,
                             fg_color="#887FFF")

        label.grid(row=2, column=1, padx=10, pady=10)

        notebook = ctk.CTkNotebook(master=self)
        notebook.grid(row=3, column=1, padx=10, pady=10)

    def btn_click(self):
        self.btn.configure(text="Test 2")


if __name__ == "__main__":
    app = App()
    app.mainloop()
