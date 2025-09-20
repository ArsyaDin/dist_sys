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
![Compose MQTT](/Assets/Proses.png)

Jika sudah terlihat tampilan seperti di atas, maka semua container yang telah dibuat berjalan dengan lancar

- - -

Jalankan perintah di bawah ini untuk menjalankan Publisher MQTT

```bash
docker compose -f compose/mqtt.yml exec mqtt-pub python pub.py
```

![](/Assets/Pub_MQTT.png)

Publisher kemudian akan publish pesan seperti yang ada pada gambar di atas

- - -

Jalankan perintah di bawah ini untuk menjalankan Subscriber MQTT

```bash
docker compose -f compose/mqtt.yml exec mqtt-sub python sub.py
```

![](/Assets/Sub_MQTT.png)

Kemudian Subscriber akan mendengarkan pesan dengan topik “sister/temp”

- - -