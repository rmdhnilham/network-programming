import json
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 1234)
print(f"connecting to {server_address}")
sock.connect(server_address)

mess = input()
cstring = mess.split(" ")

try:
    data = json.dumps(dict(perintah=cstring[0], filename=cstring[1]))+"xx"

    print("Data yang dikirim dalam format json:")
    print(data)

    sock.send(data.encode())
    data = sock.recv(1000).decode()

    if data!="null":
        with open("client-storage/download_"+cstring[1], 'wb') as file_receive:
            while True:
                diterima = sock.recv(1024)
                if not diterima:
                    print("file berhasil didownload")
                    break
                file_receive.write(diterima)
        file_receive.close()
finally:
    print("closing")
    sock.close()
