#!/bin/bash
# menjalankan chaos testing untuk mensimulasikan bencana pada sistem monitoring
sleep 20 

echo "🔥 [SISTEM] Bencana dimulai: Database Server Crash!"
mv sistem_monitoring.db database_rusak.db

# Biarkan server error dan Grafana naik selama 15 detik
sleep 15 

echo "✅ [SISTEM] Pemulihan selesai: Database Server Restarted."
mv database_rusak.db sistem_monitoring.db