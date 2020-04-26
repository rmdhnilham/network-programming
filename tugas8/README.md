**Nama**  : Ramadhan Ilham Irfany<br>
**NRP**   : 05111740000121<br>
**Kelas** : Progjar - B

# Tugas 8
### Tahap persiapan
1. Updatelah kembali repository rm77
2. Buka folder progjar5
3. Dalam file http.py, telah ada implementasi method post yang masih kosong
4. Jalankan server pada ip 127.0.0.1 dengan port 10002
[](Dokumentasi/port.PNG)

### Tahap praktik
5. Bukalah browser arahkan ke http://127.0.0.1:10002/sending.html, isilah dengan sesuatu dan kirim 
- Keterangan: sending.html merupakan file dengan format HTML yang dapat digunakan untuk mengambil input dari client dan mengirimkannya ke server
[](Dokumentasi/before_modif.PNG)

6. Akan keluar tulisan ‘kosong’
[](Dokumentasi/result_before.PNG)

7. Modifikasilah agar server dapat membalas dengan isi
[](Dokumentasi/after_modif.PNG)

- semua  header yang dikirim dari browser
[](Dokumentasi/header_sent.PNG)
[](Dokumentasi/header_inspect.PNG)

- Yang anda isikan di form pada saat mengisi pada poin nomor 5, misalkan mengisi “ISILAH” maka server akan mereply dengan “ISILAH” juga , dan bukan ‘kosong’. Disini saya mengisi ‘wony’
[](Dokumentasi/result_after.PNG)