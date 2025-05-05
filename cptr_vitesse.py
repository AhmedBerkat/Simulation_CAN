import can
import time
import random
from common import encoder_msg
bus = can.Bus(interface='socketcan', channel='vcan0')

while True:
    vit = random.randint(0, 180)
    data = encoder_msg("capteur_vitesse", {"vitesse": vit}) 
    msg = can.Message(arbitration_id=0x101, data=data, is_extended_id=False)
    bus.send(msg)
    print(f"[Capteur Vitesse] Vitesse: {vit} km/h")
    time.sleep(1)