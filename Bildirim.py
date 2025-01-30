import time
from datetime import datetime
from plyer import notification

# Hedef zamanı belirle (örn: 14:30:00)
hedef_saat = "03:22:40"

while True:
    suanki_zaman = datetime.now().strftime("%H:%M:%S")
    if suanki_zaman == hedef_saat:
        notification.notify(
            title="UYU!",  #başlık
            message="siktirgit uyu!", #içeriği 
            timeout=5
        )
        break  # Döngüyü sonlandır
    time.sleep(1)  # Her saniye kontrol et
