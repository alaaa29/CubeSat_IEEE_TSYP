from machine import Pin
import time
import dht

# --- Pin Setup ---
sensor1 = dht.DHT22(Pin(15))
sensor2 = dht.DHT22(Pin(16))
led_mode = Pin(14, Pin.OUT)      # Indicates Sensor2 mode
heater = Pin(12, Pin.OUT)        # Heater control
led_heater = Pin(11, Pin.OUT)    # LED for heater
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

# --- State ---
use_sensor1 = True
LOW_TEMP_THRESHOLD = 0.0  # Turn on heater below this temperature

def read_sensor(sensor, name):
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"{name} -> Temp: {temp:.1f}°C, Humidity: {hum:.1f}%")

        # Heater control
        if temp < LOW_TEMP_THRESHOLD:
            heater.value(1)
            led_heater.value(1)
            print("⚠️ Temperature too low — heater ON")
        else:
            heater.value(0)
            led_heater.value(0)
        return temp
    except OSError as e:
        print(f"Failed to read {name}: {e}")
        return None

print("System ready. Sensor1 active. Flip switch to activate Sensor2.")

while True:
    if button.value() == 1:  # Switch ON
        use_sensor1 = False
        led_mode.value(1)  # LED ON for Sensor2 mode
    else:
        use_sensor1 = True
        led_mode.value(0)  # LED OFF for Sensor1 mode

    if use_sensor1:
        read_sensor(sensor1, "Sensor1")
    else:
        read_sensor(sensor2, "Sensor2")

    time.sleep(2)

