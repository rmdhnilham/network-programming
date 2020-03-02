import socket
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

pesan = "Ini pesan"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(pesan.encode()),(TARGET_IP, TARGET_PORT))
