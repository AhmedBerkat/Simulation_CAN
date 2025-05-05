import can
import time
import random
from common import encoder_msg
bus = can.Bus(interface='socketcan', channel='vcan0')

while True:
    pres= random.randint(25, 80)
    data = encoder_msg("capteur_pression", {"pression": pres})
    msg = can.Message(arbitration_id=0x102, data=data, is_extended_id=False)
    bus.send(msg)
    print(f"[Capteur Pression] Pression: {pres}psi")
    time.sleep(2)
