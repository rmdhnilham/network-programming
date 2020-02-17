import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 31000)
print("Starting up on {0} port {1}".format(server_address[0], server_address[1]))
print("===================================")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection")
    connection, client_address = sock.accept()
    print(f"==> Accepted connection from {client_address}")

    # Open file for writing
    f = open("server-storage/file_received.pdf", "wb")

    print(f"==> Receiving the file from client")
    while True:
        data = connection.recv(1024)
        if data:
            f.write(data)
        else:
            f.close()
            break

    # Confirming the file has received
    msg = b"Server has received the file"
    connection.sendall(msg)

    # Clean up the connection
    connection.close()