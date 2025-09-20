# RPC Steps by step

## 1. Membuat Container 
Jalankan perintah ini pada terminal untuk membuat Docker Container
```bash
docker compose -f compose/rest.yml up -d	
```
Tunggu hingga muncul pesan seperti
![](/REST/Assets/Compose.png)
- - -

## 2. Mengecek Proses
Untuk memastikan bahwa container yang telah dibuat sebelumnya berjalan, anda dapat menjalankan perintah
```bash
docker ps
```
![](/REST/Assets/Process.png)
- - -

## 3. Menjalankan Service
Jalankan perintah di bawah ini untuk menjalankan Server REST
```bash
docker compose -f compose/rest.yml exec rest-server python server.py
```
![](/REST/Assets/Server.png)

Setelah Server dijalankan, jalankan juga perintah di bawah ini untuk memanggil Client yang akan memberikan permintaan kepada Server 
```bash
docker compose -f compose/rest.yml exec rest-client python client.py --op both -a 2 -b 3
```
- - -
Permintaan yang dikirimkan pada Server berupa kedua operasi yang terdapat pada client.py
![](/REST/Assets/Op.png)

Kemudian Server akan merespon dengan menjalankan 
![](/REST/Assets/add.png)
![](/REST/Assets/mult.png)

Lalu dari client.py akan menampilkan balasan dari bagian Server seperti di bawah ini

![](/REST/Assets/Result_Client.png)

Operasi lain dapat dilakukan sesuai dengan apa yang tersedia pada kode program "server.py" dengan mengganti parameter seperti
```bash
--op add
--op mul
--op both
```
- - -


## 4. Packet Capture
Gunakan perintah di bawah ini untuk mendapatkan informasi terkait Interface Bridge
```bash
ip a
```
![](/REST/Assets/BI.png)
- - -
Untuk menangkap paket yang kemudian akan disimpan pada file REST.pcap, gunakan kode ini
```bash
sudo tcpdump -nvi [your Interface Bridge] -w REST.pcap
```
Lalu hentikan penangkapan paket dengan menggunakan kombinasi kunci CTRL+C sehingga muncul tampilan seperti di bawah ini

![](/REST/Assets/packet.png)
- - -
Paket yang sudah disimpan dalam file REST.pcap tadi kemudian dapat dibuka dan dibaca pesan di dalamnya menggunakan Wireshark
![](/REST/Assets/WS.png)
- - -

## 5. Stopping Operation
Untuk menghentikan servis, dapat dijalankan perintah
```bash
docker compose -f compose/rest.yml down
```
tunggu hingga muncul pesan

![](/REST/Assets/stop.png)

