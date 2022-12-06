import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from datetime import date, datetime


today = datetime.today().strftime("%d/%m/%Y %H:%M Uhr")

print("Today's date:", today)


window_height = 550
window_width = 800

conversations = ['Klaus', 'Peter', 'Julia', 'Paul', 'Simon', 'Gustav', 'Gruppenchat', 'BesteGruppe', 'BackGroup',
                 'Klassenchat', 'Herbert']
num_of_conversation = len(conversations)
messages_from_server = ["Hi wie geht's, wie steht's?", "wow", "hahah", "Mir geht's ganz gut soweit. Und dir?",
                        "123456789012345678901234567890123456789012345678901234567890", "message6", "message7",
                        "message8", "message9", "message10", "message11", "message12", "message13", "message14"]
global number_of_messages
number_of_messages = len(messages_from_server)

messages_directory_showcase = {
    "conversation": {
        "date": {
            "user":
                "message"
        }
    }
}

messages_directory = {
    "conversation": {
        "date": {
            "user":
                "message"
        }
    }
}


# Method to display messages in the console when clicked
def message_clicked(msg_index):
    print(msg_index)


# Method to display the choosen conversation in the chat frame
def display_conversation(conversation_index):
    print(conversation_index)


# Method to send a message
def send_message(msg_frame, message, entry):
    print(entry.get())
    entry.delete(0, 'end')
    pass
# TODO: Send button muss den MessageFrame mit übergeben (method(self)) und dann dadurch kann abgefangen werden,
# welche Conversation sich gerade offen befindet


# Frame in which is the chat
class ChatFrame(ctk.CTkFrame):
    def __init__(self, master=None, color="#28192e"):
        super().__init__(master, bg_color=color, fg_color=color, bg=color)

        self.conversation_title = ctk.CTkLabel(self, text="Chat with: " + conversations[0],
                                               text_font=("Arial", 22, "bold"), width=519, height=40,
                                               bg_color=color, fg_color=color)
        self.conversation_title.pack(side="top", fill="both", anchor="w")

        self.msg_send_frame = ctk.CTkFrame(self, width=520, height=100, bg_color=color)
        self.msg_send_frame.pack(side="bottom", pady=10, padx=20, anchor="sw")

        self.message_input = ctk.CTkEntry(self.msg_send_frame, width=400, height=30)
        # self.message_input = ctk.CTkTextbox(self.msg_send_frame, width=400, height=1)
        self.message_input.grid(column=0, row=0, pady=10, padx=10)

        self.message_input.insert(0, "Type your message here")

        self.messages_frame = ctk.CTkFrame(self, width=540, height=400, bg_color=color)
        self.messages_frame.pack(side="right", fill="both", anchor="e")

        self.msg_frame_class = MessageFrame(self.messages_frame)

        self.msg_send_btn = ctk.CTkButton(self.msg_send_frame, text="Send", width=10, height=29,
                                          command=lambda msg_input=self.message_input.get(): send_message(self.msg_frame_class,
                                                                                                          self.message_input))
        self.msg_send_btn.grid(column=1, row=0, pady=10, padx=8)


class MessageFrame():

    def __init__(self, parent, color="#28192e", *args, **kwargs):
        super().__init__(*args, **kwargs)
        global number_of_messages

        self.canv = ctk.CTkCanvas(parent, bg=color)
        self.canv.config(width=525, height=100)

        # scrollregion has to be larger than canvas size
        # otherwise it just stays in the visible canvas
        self.canv.config(scrollregion=(0, 0, 200, number_of_messages * 50))
        self.canv.config(highlightthickness=0)
        if number_of_messages > 7:
            self.ybar = ttk.Scrollbar(parent)
            self.ybar.config(command=self.canv.yview)
            # connect the two widgets together
            self.canv.config(yscrollcommand=self.ybar.set)
            self.ybar.pack(side=RIGHT, fill=Y)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)
        self.abstand = 0

        for i, msg in enumerate(messages_from_server):
            self.msg = msg

            # if the message is longer than 40 characters, it will be split into two lines
            if len(self.msg) > 40:
                number_of_messages += 1
                self.frm = ctk.CTkFrame(parent, width=960, height=100, bg=color, bd=0)
                msg = self.msg[:40] + "\n" + self.msg[40:]
                self.msg = ctk.CTkButton(self.frm, text=msg, corner_radius=15, bg_color=color,
                                         command=lambda msg_=self.msg: message_clicked(msg_),
                                         border_color="#453847", border_width=2,
                                         hover=False, fg_color="#1f192e").grid(sticky="w")
                self.canv.create_window(20, 10 + (50 * i), anchor=NW, window=self.frm)

                self.abstand += 14
            else:
                self.frm = ctk.CTkFrame(parent, width=960, height=100, bg=color, bd=0)
                self.msg = ctk.CTkButton(self.frm, text=msg, corner_radius=25, bg_color=color,
                                         command=lambda msg_=self.msg: message_clicked(msg_),
                                         border_color="#453847", border_width=2,
                                         hover=False, fg_color="#1f192e").grid(sticky="w")
                self.canv.create_window(20, 10 + (50 * i) + self.abstand, anchor=NW, window=self.frm)
        self.canv.config(scrollregion=(0, 0, 200, number_of_messages * 47))


# Frame in which is the conversation list
class Conversation_List(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.conversation_list_header = ctk.CTkLabel(self, text="Conversations", text_font=("Arial", 18, "bold"),
                                                     width=260)
        self.conversation_list_header.pack(side="top", fill="x", pady=6, padx=10, anchor="n")
        Conversation_Buttons(self)

        self.configure(fg_color="#1f192e",
                       border_color="#3e325d",
                       border_width=2,
                       corner_radius=0,
                       width=260)


class Conversation_Buttons:
    def __init__(self, parent, color="#1f192e"):
        self.parent = parent
        self.color = color

        self.canv = ctk.CTkCanvas(self.parent, bg=self.color)
        self.canv.config(width=300, height=200)

        # scrollregion has to be larger than canvas size
        # otherwise it just stays in the visible canvas
        if num_of_conversation > 8:
            self.canv.config(scrollregion=(0, 0, 300, num_of_conversation * 62))
            self.canv.config(highlightthickness=0)

            self.ybar = ttk.Scrollbar(self.parent)
            self.ybar.config(command=self.canv.yview)
            # connect the two widgets together
            self.canv.config(yscrollcommand=self.ybar.set)
            self.ybar.pack(side=RIGHT, fill=Y)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for i, cvs in enumerate(conversations):
            self.cvs = cvs
            self.conversations_frame = ctk.CTkFrame(self.canv, width=960, height=100, fg_color="#1f192e")
            self.chats = ctk.CTkButton(self.conversations_frame, text=cvs, width=230, height=50, corner_radius=5,
                                       border_width=2, fg_color="#453847", text_font=("Arial", 16, "bold"),
                                       command=lambda cvs_=cvs: display_conversation(cvs_)).grid()
            self.canv.create_window(10, 3 + (62 * i), anchor=NW, window=self.conversations_frame)

        # TODO: Function to add new conversation


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
