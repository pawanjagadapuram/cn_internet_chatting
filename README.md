Project Name: IMPLEMENTATION OF INTERNET CHATTING

This zip file holds a repository that implements the Internet Chatting with file transfer.

Problem Statement:

Implement a simple internet chat program, which will create two threads: a main thread (also used as the reading thread) and a writing thread.
When the program starts, the main thread executes the following: First, it creates a new thread – let’s call it the writing thread.
This thread will take a port number from the keyboard and then connects to that port number. After the connection (socket) is
successfully established, it goes into a loop of reading  a message from the keyboard and writing the message to the connection (socket).
If the message is ”transfer filename”, after the message is written, the file is transmitted through the connection. Next, it creates
a ServerSocket, prints out the port number used, and listens on the socket for new connection (i.e. the accept method). When a new 
connection from another user arrives, the connection Socket is established. The main thread will become the so-called reading thread 
by listening to the connection socket. This thread will attempt to read messages from the connection socket and print the messages on the screen. 
If the message is “transfer filename”, it reads the file and stores locally. 


Running program in cmd:

1. Alice --> python chat_program.py
2. Bob --> python chat_program.py

Test Case1:

Start Alice on one cmd window
Start Bob on another cmd window
Enter the target port number on Alice window: Look for the listening port of Bob
Enter the target port number on Bob window: Look for the listening port of Alice
Enter messages from Alice window and they should appear on Bob's window.
Enter messages from Bob window and they should appear on Alice's window.
Enter command: transfer filename from any of the windows and make sure the file is transferred successfully.

Note: The files to be transferred should be in the same folder as in the chat_program python program. 