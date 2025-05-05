import can
from common import decoder_msg

bus = can.Bus(interface='socketcan', channel='vcan0')
print("[Ventilateur] en attente de signal ")

while True:
    msg = bus.recv()
    nom, sig = decoder_msg(msg.data, msg.arbitration_id)
    if nom == "actionneur_ventilateur" and sig["ven_active"] == 1:
        print("[Ventilateur] active")
