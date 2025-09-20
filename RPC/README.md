# RPC Steps by step

## 1. Membuat Container 
Jalankan perintah ini pada terminal untuk membuat Docker Container
```bash
 docker compose -f compose/rpc.yml up -d
```
![](/RPC/Assets/Built_image.png)
- - -

## 2. Mengecek Proses
Untuk memastikan bahwa container yang telah dibuat sebelumnya berjalan, anda dapat menjalankan perintah
```bash
docker ps
```
![](/RPC/Assets/RPC_Process.png)
- - -

## 3. Menjalankan Service
Jalankan perintah di bawah ini untuk menjalankan Server & Client RPC
```bash
docker compose -f compose/rpc.yml exec rpc-server python rpcserver.py
docker compose -f compose/rpc.yml exec rpc-client python rpcclient.py
```
- - -
Client akan memanggil permintaan yang terdapat pada rpcclient.py seperti yang ada pada gambar di bawah

![](/RPC/Assets/Client_op.png)
- - -
Kemudian Server akan menjawab dengan menjalankan operasi ini

![](/RPC/Assets/Server_op.png)
- - -
Terminal akan menampilkan pesan yang didapat oleh Server dan juga hasil dari operasi permintaan Client
![](/RPC/Assets/RPC_Server.png)
![](/RPC/Assets/RPC_Client.png)
- - -

## 4. Packet Capture
Gunakan perintah di bawah ini untuk mendapatkan informasi terkait Interface Bridge
```bash
ip a
```
![](/RPC/Assets/IB.png)
- - -
Untuk menangkap paket yang kemudian akan disimpan pada file RPC.pcap, gunakan kode ini
```bash
sudo tcpdump -nvi [your Interface Bridge] -w RPC.pcap
```
Lalu hentikan penangkapan paket dengan menggunakan kombinasi kunci CTRL+C sehingga muncul tampilan seperti gambar di bawah ini
![](/RPC/Assets/packet_capture.png)
- - -
Paket yang sudah disimpan dalam file RPC.pcap tadi kemudian dapat dibuka dan dibaca pesan di dalamnya menggunakan Wireshark
![](/RPC/Assets/WS_RPC.png)
- - -

## 5 Modification
Sedikit modifikasi dilakukan dengan membuat file baru bernama rpcclientNew.py

Untuk menjalankan servis tersebut maka jalankan perintah
```bash
docker compose -f compose/rpc.yml exec rpc-client python rpcclientNew.py
```

Modifikasi dilakukan pada permintaan seperti gambar di bawah ini yang kemudian akan ditanggung Server
![](/RPC/Assets/Client_Req_new.png)
- - -
Kemudian Server akan membalas permintaan Client dengan memberikan jawaban sesuai operasi yang diminta

![](/RPC/Assets/Client_new.png)

## 6. Stopping Operation
Untuk menghentikan servis, dapat dijalankan perintah
```bash
docker compose -f compose/rpc.yml down
```
tunggu hingga muncul pesan

![](/RPC/Assets/Stop_msg.png)

