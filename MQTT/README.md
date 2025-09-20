# MQTT: Steps by Step
Jalankan perintah ini pada terminal untuk membuat Docker Container 

```bash
docker compose -f compose/mqtt.yml up -d
```
![Compose MQTT](/Assets/Compose_MQTT.png)

Setelah perintah dijalankan, maka akan muncul pemberitahuan seperti diatas yang menandakan bahwa semua service telah dibuat

- - -

Untuk memastikan bahwa container yang telah dibuat sebelumnya berjalan, anda dapat menjalankan perintah

```bash
docker ps
```
![Prose Container MQTT](/Assets/Proses.png)

Jika sudah terlihat tampilan seperti di atas, maka semua container yang telah dibuat berjalan dengan lancar

- - -

Jalankan perintah di bawah ini untuk menjalankan Publisher MQTT

```bash
docker compose -f compose/mqtt.yml exec mqtt-pub python pub.py
```

![Publisher MQTT](/Assets/Pub_MQTT.png)

Publisher kemudian akan publish pesan seperti yang ada pada gambar di atas

- - -

Jalankan perintah di bawah ini untuk menjalankan Subscriber MQTT

```bash
docker compose -f compose/mqtt.yml exec mqtt-sub python sub.py
```

![Subscriber MQTT](/Assets/Sub_MQTT.png)

Kemudian Subscriber akan mendengarkan pesan dengan topik “sister/temp”

- - -

Jika Publisher dan Subscriber dijalankan bersamaan pada dua terminal yang terpisah, maka akan terlihat seperti gambar di bawah ini

![](/Assets/Tampilan.png)

Publisher mengirimkan pesan terus menerus yang kemudian akan diterima oleh Subscriber dan ditampilkan pada terminal.
- - -
## Modification
Di sini modifikasi dilakukan dengan mengganti topic menjadi “sister/temp/athonk” dan suhu menjadi 30 pada pub.py

![](/Assets/Mod.png)

![](/Assets/Sub_Mod.png)

Publisher berhasil mengirimkan pesan berupa “Suhu: 30℃”, namun Subscriber tidak menerima pesan apapun. Hal tersebut dikarenakan Subscriber tidak berlangganan topik yang sama dengan Publisher
- - -

Untuk karena itu, topic pada file sub.py harus disamakan seperti pada pub.py

![](/Assets/Mod_topic.png)
![](/Assets/Mod_sub.png)

Sehingga Subscriber dapat menerima pesan dari Publisher seperti tampilan di atas

## Capturing Packet
Gunakan perintah di bawah ini untuk mendapatkan informasi terkait Interface Bridge
- - -

```bash
ip a
```

![](/Assets/Interface_Bridge.png)

Interface Bridge seperti gambar di atas kemudian akan kita gunakan untuk menangkap paket yang berada pada interface tersebut
- - -
Untuk menangkap paket yang kemudian akan disimpan pada file MQTT.pcap, gunakan kode ini
```bash
sudo tcpdump -nvi [your Interface Bridge] -w MQTT.pcap
```
Lalu hentikan penangkapan paket dengan menggunakan kombinasi kunci CTRL+C sehingga muncul tampilan seperti gambar di bawah ini

![](/Assets/Packet_capt.png)
- - -

![](/Assets/wireshark.png)

Paket yang sudah disimpan tadi kemudian dapat dibuka dan dibaca pesan di dalamnya menggunakan Wireshark

- - -
## Add On
Berikut ini percobaan untuk menambahkan Publisher baru dengan topik yang sama dengan pub.py, dengan membuat file baru bernama pub_new.py 

yang kemudian dijalankan service nya menggunakan perintah

```bash
docker compose -f compose/mqtt.yml exec mqtt-pub python pub_new.py
```
![](/Assets/Pub_New_MQTT.png)

Ketika Publisher baru dan Subscriber dijalankan bersamaan pada dua terminal yang terpisah, maka akan tampilan terminal akan terlihat seperti pada gambar di atas
- - -

![](/Assets/Sub_New_MQTT.png)

Dikarenakan pub_new.py memiliki topik yang sama dengan pub.py, Subscriber dapat menerima pesan dari kedua Publisher sekaligus