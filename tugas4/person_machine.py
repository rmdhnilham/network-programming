from person import Person
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER...

FITUR

- upload : untuk meletakkan file yang dikirim oleh client
  request : upload
  parameter : [nama file].[ekstensi]
  response : berhasil -> OK
             gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar file yang ada

- download : untuk mencari file berdasar nama yang akan dikirimkan ke client
  request: download
  parameter: [nama file].[ekstensi]
  response: file yang dicari

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Person()

class PersonMachine:
    def proses(self,string_to_process):
        try:
            command = string_to_process.copy()
            if (command['perintah']=='upload'):
                logging.warning("upload")
                nama = command['filename']
                size = command['filesize']
                type = command['filetype']
                p.upload_data(nama,size,type)
                return "OK"
            elif (command['perintah']=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (command['perintah']=='download'):
                logging.warning("download")
                nama = command['filename']
                hasil = p.download_data(nama)
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"
