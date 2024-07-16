import RPi.GPIO as GPIO
import time

# GPIO-Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# GPIO-Pin festlegen
LED_PIN = 18

# Pin als Ausgang festlegen
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED an
        time.sleep(1)  # 1 Sekunde warten
        GPIO.output(LED_PIN, GPIO.LOW)   # LED aus
        time.sleep(1)  # 1 Sekunde warten
except KeyboardInterrupt:
    print("Beenden...")

# Kleine änderung
# Mal schauen was wird
