import socket
from tkinter import *
import threading

# Create the main window for the server
root = Tk()
root.title("Chat Server")
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

# Set up socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = 'localhost'
PORT = 12345

server_socket.bind((HOST_NAME, PORT))
server_socket.listen(5)

# Function to send message from server
def send_message(client):
    message = entry.get()
    if message != "":
        listbox.insert(END, "You (Server): " + message)  # Add message to Listbox
        entry.delete(0, END)  # Clear the entry field
        client.send(message.encode())  # Send to client

# Function to handle the client connection
def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()  # Wait for message from client
            if message:
                listbox.insert(END, "Client: " + message)  # Display client message
                root.after(0, root.update())  # Ensure UI updates properly
        except:
            break

def listen_for_client():
    global client
    client, address = server_socket.accept()
    listbox.insert(END, "Client connected!")
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()

# Start listening for the client in a separate thread
threading.Thread(target=listen_for_client, daemon=True).start()

# Button to send the message
button = Button(root, text="Send", width=10, command=lambda: send_message(client))
button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
