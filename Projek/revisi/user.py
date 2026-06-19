import requests, time

print("User bot berjalan. Mengirim transaksi normal setiap detik...")
while True:
    try:
        res = requests.get("http://127.0.0.1:5000/bayar")
        if res.status_code == 200:
            print(" -> User: Transaksi Sukses")
        else:
            print(" -> User: Transaksi Gagal")
    except:
        pass
    time.sleep(1)