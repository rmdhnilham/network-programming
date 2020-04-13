import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 10001


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP,TARGET_PORT)
        self.sock.connect(self.server_address)
    def sendstring(self,string):
        if string == "GET / HTTP/1.0":
            string = string + " \r\n\r\n"
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(32)
                print("diterima dari server")
                if (data):
                    receivemsg = data.decode()  #data harus didecode agar dapat di operasikan dalam bentuk string
                    if receivemsg[-4:]=='\r\n\r\n':
                        print("Pesan:")
                        return receivemsg
        except:
            self.sock.close()
            return "Error, gagal"



if __name__=="__main__":
    cc = ChatClient()
    print("Http Protocol\n")
    # tes = "GET / HTTP/1.0 \r\n"
    request = input("Request: ")
    print(cc.sendstring(request))