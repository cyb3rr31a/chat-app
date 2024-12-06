import socket
from tkinter import *
import threading

# Create the main window for the client
root = Tk()
root.title("Chat Client")
root.geometry("400x500")

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

# Set up socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = 'localhost'
PORT = 12345

# Connect to the server
client.connect((HOST_NAME, PORT))

# Function to send message from client
def send_message():
    message = entry.get()
    if message != "":
        listbox.insert(END, "You (Client): " + message)  # Add message to Listbox
        entry.delete(0, END)  # Clear the entry field
        client.send(message.encode())  # Send to server

# Function to listen for messages from the server
def listen_for_server():
    while True:
        try:
            message = client.recv(1024).decode()  # Wait for message from server
            if message:
                listbox.insert(END, "Server: " + message)  # Display server message
                root.after(0, root.update())  # Ensure UI updates properly
        except:
            break

# Start listening for the server in a separate thread
threading.Thread(target=listen_for_server, daemon=True).start()

# Button to send the message
button = Button(root, text="Send", width=10, command=send_message)
button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
