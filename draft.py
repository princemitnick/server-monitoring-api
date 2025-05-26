import psutil
import time

net1 = psutil.net_io_counters()
time.sleep(1)
net2 = psutil.net_io_counters()

# Calcul du débit montant (upload) en octets/sec
upload = net2.bytes_sent - net1.bytes_sent
download = net2.bytes_recv - net1.bytes_recv

print(f"Upload: {upload} B/s")
print(f"Download: {download} B/s")