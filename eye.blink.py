import time
from plyer import notification
while True:
	notification.notify(title="Blink ur Eye 20 times",
                         message ="Blinking eyes is a good practice",
                         timeout=30 )
	time.sleep(20*60)
