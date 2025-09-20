import paho.mqtt.client as mqtt
import time
import sys
import math

# Gunakan broker lokal dalam docker compose
broker = "mqtt-broker"
port = 1883  # Port default untuk MQTT

# Inisialisasi topik
topic = "sister/temp/athonk"

# Callback untuk koneksi
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Berhasil terhubung ke broker MQTT {broker}")
    else:
        print(f"Gagal terhubung ke broker, kode error: {rc}")
        sys.exit(1)

# Inisialisasi klien MQTT dengan API versi terbaru
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

# Menghubungkan ke broker
try:    
    print(f"Menghubungkan ke {broker}...")
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"Gagal menghubungkan ke broker: {e}")
    sys.exit(1)

# Loop untuk mengirim pesan setiap detik
try:
    n = 0              # iterasi waktu
    a = 1              # nilai awal
    b = 1.2            # faktor pertumbuhan (20% per langkah)
    
    while True:
        # Fungsi eksponensial
        value = a * (b ** n)
        
        # Format pesan
        message = f"Iterasi {n} | Nilai eksponensial: {value:.2f}"
        client.publish(topic, message)
        print(f"Published: {message}")
        
        # Tunggu 1 detik
        time.sleep(1)
        n += 1

except KeyboardInterrupt:
    print("Publisher dihentikan.")
    client.disconnect()
