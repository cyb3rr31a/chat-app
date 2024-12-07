# Chat Application with GUI

This program is a simple **chat application** that enables communication between a server and a client using **Tkinter** for the graphical user interface (GUI) and **sockets** for network communication. It allows the server and client to exchange messages in real-time, with the chat history displayed in a scrollable interface.

---

## Features

- **GUI for Server and Client**:
  - User-friendly graphical interface built using Tkinter.
  - Scrollable chat history displayed in a `Listbox`.
  
- **Real-time Communication**:
  - Bi-directional message exchange between server and client over a TCP connection.

- **Threading**:
  - Concurrent handling of message sending/receiving ensures the GUI remains responsive.

- **Customizable**:
  - Easily adaptable to connect across networks by changing the IP address.

---

## Requirements

1. Python 3.x
2. Modules:
   - `socket`
   - `threading`
   - `tkinter` (built-in for Python on most systems)

---

## How to Run

### **Server Setup**

1. Run the `server.py` file:
   ```bash
   python server.py
   ```
2. The server GUI will open, and it will wait for a client to connect.

---

### **Client Setup**

1. Run the `client.py` file:
   ```bash
   python client.py
   ```
2. The client GUI will open and connect to the server.

---

## Usage

1. **Server**:
   - Type a message in the input field and click "Send" or press Enter to send the message to the client.
   - Messages from the client will automatically appear in the chat history.

2. **Client**:
   - Type a message in the input field and click "Send" or press Enter to send the message to the server.
   - Messages from the server will appear in the chat history.

---

## Code Overview

### **Server**

- Sets up a socket to listen for client connections.
- Handles client messages in a separate thread.
- Allows sending messages to the connected client through the GUI.

### **Client**

- Connects to the server socket.
- Sends messages to the server through the GUI.
- Listens for messages from the server in a separate thread.

---

## Customization

- **Change Port or IP Address**:
  - Modify the `HOST_NAME` and `PORT` variables in both `server.py` and `client.py` to set a specific IP address and port.
  - Example for running across a network:
    - Server `HOST_NAME`: Public/Private IP of the server.
    - Client `HOST_NAME`: Same IP as the server.

---

## Troubleshooting

- **Port Already in Use**:
  - Ensure the specified port is not used by another application.
  - Use tools like `netstat` to check port status.

- **Firewall Issues**:
  - Ensure your firewall allows traffic on the specified port.

- **Connection Error**:
  - Verify the server is running and accessible from the client machine.
  - Confirm IP address and port match on both client and server.

---

## Acknowledgments

This application demonstrates the fundamentals of:

1. Networking with Python's `socket` module.
2. GUI development with Tkinter.
3. Multi-threaded programming for handling concurrent tasks.

Feel free to extend and adapt this program to suit your needs!
