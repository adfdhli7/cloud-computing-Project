import boto3
import time
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

print("=== MANUAL INJECTION TERMINAL ===")
print("Ketik '1' untuk mengirim manual log [INFO]")
print("Ketik '0' untuk mengirim manual log [ERROR]")
print("Ketik 'x' untuk menghentikan program.\n")

try:
    while True:
        perintah = input(">> ")
        
        # Mengambil waktu persis saat tombol Enter ditekan
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if perintah.lower() == '1':
            pesan = "[INFO] Transaction OK - simulasi transaksi manual"
            put_log(pesan)
            print(f"[{waktu}]  -->  MANUAL TERKIRIM: {pesan}")
            
        elif perintah.lower() == '0':
            pesan = "[ERROR] Payment Gateway Timeout - simulasi transaksi manual"
            put_log(pesan)
            print(f"[{waktu}]  -->  MANUAL TERKIRIM: {pesan}")
            
        elif perintah.lower() == 'x':
            print("Menghentikan terminal manual...")
            break
        else:
            print("  --> Perintah tidak dikenali. Ketik 'sukses', 'gagal', atau 'exit'.")
except KeyboardInterrupt:
    print("\nTerminal manual ditutup.")



