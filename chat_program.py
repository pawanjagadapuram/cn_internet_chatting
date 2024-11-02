import socket
import threading
import sys
import os

BUFFER_SIZE = 1024

def writing_thread(connection_socket):
    while True:
        message = input()
        connection_socket.sendall(message.encode())

        if message.startswith("transfer"):
            _, filename = message.split()
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    file_data = file.read(BUFFER_SIZE)
                    while file_data:
                        connection_socket.send(file_data)
                        file_data = file.read(BUFFER_SIZE)
            else:
                print("File not found.")

def main():
    # Create a ServerSocket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 0))
    server_socket.listen(1)

    # Print the port number used
    port = server_socket.getsockname()[1]
    print(f"Listening on port: {port}")

    # Connect to another user
    target_port = int(input("Enter the target port number: "))
    connection_socket = socket.create_connection(("localhost", target_port))

    # Start the writing thread
    threading.Thread(target=writing_thread, args=(connection_socket,)).start()

    # Accept a new connection and become the reading thread
    client_socket, _ = server_socket.accept()

    while True:
        received_data = client_socket.recv(BUFFER_SIZE)
        message = received_data.decode()

        if message.startswith("transfer"):
            _, filename = message.split()
            with open("new"+filename, "wb") as file:
                file_data = client_socket.recv(BUFFER_SIZE)
                while file_data:
                    file.write(file_data)
                    file_data = client_socket.recv(BUFFER_SIZE)

            print(f"File '{filename}' received and saved.")
        else:
            print(message)

if __name__ == "__main__":
    main()
