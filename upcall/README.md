## 1. Membuat Container 
Jalankan perintah ini pada terminal untuk membuat Docker Container
```bash
docker compose -f compose/upcall.yml up -d	
```
Tunggu hingga muncul pesan seperti

![](/upcall/Assets/Buildd_IMG.png)
- - -

## 2. Mengecek Proses
Untuk memastikan bahwa container yang telah dibuat sebelumnya berjalan, anda dapat menjalankan perintah
```bash
docker ps
```
![](/upcall/Assets/Process.png)
- - -

## 3. Menjalankan Service
Jalankan perintah di bawah ini untuk menjalankan Server upcall
```bash
docker compose -f compose/upcall.yml exec upcall-server python clientserver.py
```
![](/upcall/Assets/Server.png)

Setelah Server dijalankan, gunakan perintah di bawah ini untuk menjalankan Client 
```bash
docker compose -f compose/upcall.yml exec upcall-client python clientcall.py
```

![](/upcall/Assets/Client_Req.png)

Kemudian Server akan menampilkan pesan yang diterima dari Client seperti ini

![](/upcall/Assets/Server_Reply.png)
- - -

## 4. Packet Capture
Gunakan perintah di bawah ini untuk mendapatkan informasi terkait Interface Bridge
```bash
ip a
```
![](/upcall/Assets/BI.png)
- - -
Untuk menangkap paket yang kemudian akan disimpan pada file upcall.pcap, gunakan kode ini
```bash
sudo tcpdump -nvi [your Interface Bridge] -w upcall.pcap
```
Lalu hentikan penangkapan paket dengan menggunakan kombinasi kunci CTRL+C sehingga muncul tampilan seperti di bawah ini

![](/upcall/Assets/Packet_capt.png)
- - -
Paket yang sudah disimpan dalam file REST.pcap tadi kemudian dapat dibuka dan dibaca pesan di dalamnya menggunakan Wireshark

![](/upcall/Assets/ws.png)
- - -

## 5. Stopping Operation
Untuk menghentikan servis, dapat dijalankan perintah
```bash
docker compose -f compose/upcall.yml down
```
tunggu hingga muncul pesan

![](/upcall/Assets/stop.png)
