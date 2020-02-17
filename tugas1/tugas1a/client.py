import sys
import socket

# Address and port where client would connect to
address_port = ("localhost", 31000)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(address_port)

# Open file
files = open("file_sent.pdf", "rb")

try:
    # Send data
    print(f"Sending file to server port {address_port[1]}")
    buff = files.read(1024)
    while buff:
        sock.send(buff)
        buff = files.read(1024)

    # Receive respond from server
    # Shutdown socket after sending files
    sock.shutdown(socket.SHUT_WR)
    buff = sock.recv(1024)

    # Print respond message
    print("[Server]: " + buff.decode('utf-8'))

finally:
    print("File sent successfully")
    # Close file
    files.close()
    
    sock.close()
    print("Connection closed")