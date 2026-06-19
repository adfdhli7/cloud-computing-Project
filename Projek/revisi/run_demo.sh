#!/bin/bash
echo "Memulai arsitektur server..."

# Menyalakan API dan Bot di latar belakang (background)
nohup python3 server_api.py > /dev/null 2>&1 &
API_PID=$!

nohup python3 bot_user.py > bot_output.txt 2>&1 &
BOT_PID=$!

# Menjalankan simulasi chaos testing untuk mensimulasikan bencana pada sistem monitoring
bash chaos.sh

# Setelah bencana dan pemulihan selesai, matikan semuanya
kill $API_PID
kill $BOT_PID
echo "Demo Selesai."