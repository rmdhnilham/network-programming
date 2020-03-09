import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

wony = ['https://i.pinimg.com/originals/9d/b5/e8/9db5e8a59752292bb96eab70e37c216e.jpg',
                'https://i.pinimg.com/originals/08/30/34/083034ffa98aeef09d075457bb4d7a9e.jpg',
                'https://i.pinimg.com/originals/56/81/2b/56812b7cfb898e7230c0a126657410f3.jpg']

if __name__=='__main__':
    threads = []
    for i in wony:
        t = threading.Thread(target=download_gambar, args=(i,))
        threads.append(t)

    for thr in threads:
        thr.start()