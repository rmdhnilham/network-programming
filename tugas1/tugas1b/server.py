import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 31001)
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

    # Store filename requested by client
    s = ""
    while True:
        data = connection.recv(1024)
        if data:
            s += data.decode("utf-8")
        else:
            break

    print("==> File requested: " + s)

    # Send the requested file
    f = open(s, "rb")
    print("==> Sending file...")

    buff = f.read(1024)
    while buff:
        connection.send(buff)
        buff = f.read(1024)

    print("==> File sent")
    # close file after reading
    f.close()

    # Clean up the connection
    connection.close()