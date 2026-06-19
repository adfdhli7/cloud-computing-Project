from flask import Flask
from datetime import datetime
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route('/bayar')
def bayar():
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # mencoba membaca database
        with open("sistem_monitoring.db", "r") as db:
            pass 
        
        pesan = f"[{waktu}] [INFO] Transaksi sukses. Database aman."
        with open("app.log", "a") as f: 
            f.write(pesan + "\n")
        return "OK", 200
        
    except FileNotFoundError:
        # transaksi gagal dan server eror, karena database tidak ditemukan
        pesan = f"[{waktu}] [ERROR] FATAL: Server Database Down! Transaksi gagal."
        with open("app.log", "a") as f: 
            f.write(pesan + "\n")
        return "ERROR", 500

if __name__ == '__main__':
    # host='0.0.0.0' agar bisa diakses dari luar jika dibutuhkan
    app.run(host='0.0.0.0', port=5000)