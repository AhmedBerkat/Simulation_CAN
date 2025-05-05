import can
from common import decoder_msg

bus = can.Bus(interface='socketcan', channel='vcan0')
print("[mTurbo] en attente de signal ")

while True:
    msg = bus.recv()
    nom, sig = decoder_msg(msg.data, msg.arbitration_id)
    if nom == "actionneur_mturbo" and sig["turbo_active"] == 1:
        print("[mTurbo] active")
