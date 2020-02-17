import sys
import socket

# Address and port where client would connect to
address_port = ("localhost", 31001)

# Filename request
file_request = "file_request.pdf"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(address_port)

try:
    # Sending file request to the server
    print(f"Requesting {file_request} to server....")
    sock.send(file_request.encode())

    # Shutdown socket to receive incoming file
    sock.shutdown(socket.SHUT_WR)

    # Write incoming file
    f = open("client-storage/file_received.pdf", "wb")
    while True:
        data = sock.recv(1024)
        if data:
            f.write(data)
        else:
            f.close()
            break
finally:
    print("File received from the server")

    # Close connection
    sock.close()
