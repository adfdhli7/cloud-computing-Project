import boto3
import time
import random
from datetime import datetime

client = boto3.client('logs', region_name='us-east-1')
log_group = '/application/payment-system'
log_stream = 'transaction-stream'

def put_log(message):
    client.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[{'timestamp': int(time.time() * 1000), 'message': message}]
    )

print("=== AUTO SIMULATOR BERJALAN ===")
print("Mengirim log otomatis... (Tekan Ctrl+C untuk berhenti)\n")

try:
    while True:
        # Mengambil waktu saat ini dan memformatnya menjadi Jam:Menit:Detik
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        peluang_error = random.random()
        if peluang_error < 0.01:
            pesan = "[ERROR] Payment Gateway Timeout - (Auto)"
            put_log(pesan)
            print(f"[{waktu}]  {pesan}")
        else:
            pesan = "[INFO] Transaction OK - (Auto)"
            put_log(pesan)
            print(f"[{waktu}]  {pesan}")
            
        jeda = random.uniform(2, 5)
        time.sleep(jeda)
except KeyboardInterrupt:
    print("\nSimulasi otomatis dihentikan.")
