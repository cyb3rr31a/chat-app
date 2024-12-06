from tkinter import *

# Create the main window
root = Tk()
root.title("Chat App")
root.geometry("300x400")  # Set the window size

# Frame for the chat history (Listbox)
frame = Frame(root)
frame.pack(pady=10)

# Scrollbar for Listbox
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Listbox to display the chat messages
listbox = Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, bd=1, selectmode=SINGLE)
listbox.pack(side=LEFT, fill=BOTH, padx=10)

# Configure scrollbar
scrollbar.config(command=listbox.yview)

# Entry widget for typing messages
entry = Entry(root, width=50)
entry.pack(pady=10, padx=10)

# Function to send message
def send_message():
    message = entry.get()
    if message != "":
        listbox.insert(END, "You: " + message)  # Add message to Listbox
        entry.delete(0, END)  # Clear the entry field

# Button to send the message
button = Button(root, text="Send", width=10, command=lambda: send_message())
button.pack(pady=5)

# Run the application
root.mainloop()
