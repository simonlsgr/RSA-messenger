import tkinter
from tkinter import *

# Create a window and configuration
window = Tk()
window.title("Messenger")
window.geometry("400x500")
window.maxsize(400, 485)
window.minsize(400, 485)

# Create a frame
frame = Frame(window)
frame.pack()

# Create 3 buttons to choose a chat server
server1 = Button(window, text="Server 1")
server1.pack()
server2 = Button(window, text="Server 2")
server2.pack()
server3 = Button(window, text="Server 3")
server3.pack()

# Create a button to exit the prgram
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=20)

# Run the main window loop
window.mainloop()
