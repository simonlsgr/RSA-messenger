import random
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Function to send message
def send():
    # Get the message from the user
    if user_input.get() != '':
        message = user_input.get()
        # Add the message to the chat window
        chat_window.config(state=NORMAL)
        chat_window.insert(END, "You: " + message + "\n")
        chat_window.config(font=("Verdana", 15), state=DISABLED)

    # Clear the user input
    user_input.delete(0, END)
    # Get the response from the bot
    response = get_response(message)
    # Add the response to the chat window
    chat_window.insert(END, "Bot: " + response + "\n")

# Function to get the bot response
def get_response():
    # Get the bot response
    response = "I don't understand"
    # Return the bot response
    return response


# Create a window
window = tk.Tk()
window.title("Messenger")
window.geometry("400x500")

# Create a frame
frame = tk.Frame(window)
frame.pack()

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a text box with input
chat_window = tk.Text(frame, width=55, height=22, yscrollcommand=scrollbar.set)
chat_window.pack(side=LEFT, fill=BOTH)

# Create an entry box
user_input = tk.Entry(window, width=50)
user_input.pack()

# Create a button to send the message
send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

# Create a button
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=20)

# Run the main window loop
window.mainloop()
