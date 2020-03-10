**Nama**  : Ramadhan Ilham Irfany<br>
**NRP**   : 05111740000121<br>
**Kelas** : Progjar - B

# Tugas 2
## Menggunakan wireshark, capture:

### Hasil keluaran dari program udpfileclient.py ke alamat 127.0.0.1 ke port 5006
1. Atur alamat IP dan port pada file udpfileclient.py dengan TARGET_IP menjadi 127.0.0.1 dan TARGET_PORT menjadi 5006

![](Dokumentasi/udpfileclient-code.png)

2. Buka wireshark, buka menu 'Adaptor Loopback traffic capture', lalu isikan filter dengan "ip.src == 127.0.0.1 && ip.dst ==127.0.0.1 && udp.port==5006" 
3. Hasil capture

![](Dokumentasi/udpfileclient-pkt.png)

### Hasil keluaran dari program udp_simple.py ke alamat 127.0.0.1 ke port 5006

1. Atur alamat IP dan port pada file udp_simple.py dengan TARGET_IP menjadi 127.0.0.1 dan TARGET_PORT menjadi 5006

![](Dokumentasi/udpsimple-code.png)

2. Buka wireshark, buka menu 'Adaptor Loopback traffic capture', lalu isikan filter dengan "ip.src == 127.0.0.1 && ip.dst ==127.0.0.1 && udp.port==5006" 
3. Hasil capture

![](Dokumentasi/udpsimple-pkt.png)

## Dengan instruksi sama, menggunakan 2 PC dalam 1 Wi-Fi:

### Hasil keluaran dari program udpfileclient.py ke alamat PC lain 10.151.254.146 ke port 5006
1. Atur alamat IP dan port pada file udpfileclient.py dengan TARGET_IP menjadi 10.151.254.146 dan TARGET_PORT menjadi 5006

![](Dokumentasi/udpfileclient_pclain.png)

2. Buka wireshark, buka menu 'WiFi', lalu isikan filter dengan "ip.src == 10.151.254.120 && ip.dst ==10.151.254.146 && udp.port==5006". 10.151.254.120 adalah alamat IP dari PC saya 
3. Hasil capture

![](Dokumentasi/udpfileclient_ws.png)

### Hasil keluaran dari program udp_simple.py ke alamat PC lain 10.151.254.146 ke port 5006

1. Atur alamat IP dan port pada file udp_simple.py dengan TARGET_IP menjadi 10.151.254.146 dan TARGET_PORT menjadi 5006

![](Dokumentasi/udpsimple_pclain.png)

2. Buka wireshark, buka menu 'WiFi', lalu isikan filter dengan "ip.src == 10.151.254.120 && ip.dst ==10.151.254.146 && udp.port==5006" 
3. Hasil capture

![](Dokumentasi/udpsimple_ws.png)

