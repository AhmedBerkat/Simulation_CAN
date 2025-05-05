import can
import time
import random
from common import encoder_msg
bus = can.Bus(interface='socketcan', channel='vcan0')

while True:
    temp = random.randint(55, 110)
    data = encoder_msg("capteur_temperature", {"temperature": temp})
    msg = can.Message(arbitration_id=0x100, data=data, is_extended_id=False)
    bus.send(msg)
    print(f"[Capteur Temp] Température: {temp}°C")
    time.sleep(1)
