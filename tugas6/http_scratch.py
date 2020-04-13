import sys
import os.path
import uuid
from glob import glob
from datetime import datetime


class httpServerScratch:
    def __init__(self):
        self.sessions = {}
        self.types = {}
        self.types['.pdf'] = 'application/pdf'
        self.types['.jpg'] = 'image/jpeg'
        self.types['.txt'] = 'text/plain'
        self.types['.html'] = 'text/html'

    def response(self, kode=404, message='Not Found', messagebody='', headers={}):
        tanggal = datetime.now().strftime('%c')
        resp = []
        resp.append("HTTP/1.0 {} {}\r\n".format(kode, message))
        resp.append("Date: {}\r\n".format(tanggal))
        resp.append("Connection: close\r\n")
        resp.append("Server: myserver/1.0\r\n")
        resp.append("Content-Length: {}\r\n".format(len(messagebody)))
        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))
        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        # print(resp)
        response_str = ''
        for i in resp:
            response_str = "{}{}".format(response_str, i)
        return response_str

    def proses(self, data):
        # data = data.decode()
        # print("Data:\n" + data)
        requests = data.split("\r\n")
        baris = requests[0]
        # print("tes:" + object_address + "hoho")
        # print("Baris:\n" + baris)
        j = baris.split(" ")
        try:
            method = j[0].upper().strip()
            if (method == 'GET'):
                object_address = j[1].strip()
                # print("Object Address:\n" + object_address)
                return self.http_get(object_address)
            else:
                return self.response(400, 'Bad Request', '', {})
        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address):
        files = glob('./*')
        thedir = './'
        if object_address == "/":
            isi = "<h1>SERVER HTTP</h1>"
            content_type = self.types['.html']
            headers = {}
            headers['Content-type'] = content_type
            # print(isi)
            # return isi
            # isi = bytes(isi, 'utf-8')
            return self.response(200, 'OK', isi, headers)

    # if thedir+object_address not in files:
    # 	return self.response(404,'Not Found','',{})
    # fp = open(thedir+object_address,'r')
    # isi = fp.read()
    #
    # fext = os.path.splitext(thedir+object_address)[1]
    # content_type = self.types[fext]
    #
    # headers={}
    # headers['Content-type']=content_type
    #
    # return self.response(200, 'OK', isi, headers)


# >>> import os.path
# >>> ext = os.path.splitext('/ak/52.png')

if __name__ == "__main__":
    httpserver = httpServerScratch()
    # d = httpserver.proses('GET testing.txt HTTP/1.0')
    # print(d)
    d = httpserver.proses('GET / HTTP/1.0')
    print(d)
# d = httpserver.http_get('testing2.txt')
# print(d)
# d = httpserver.http_get('testing.txt')
# print(d)