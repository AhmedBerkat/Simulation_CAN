import can
from common import decoder_msg, encoder_msg
from collections import deque
from can import CanError

bus = can.Bus(interface='socketcan', channel='vcan0')
file_priorite = deque()

try:
    while True:
        msg = bus.recv(timeout=0.1)
        if msg:
            file_priorite.append(msg)

        if file_priorite:
            file_priorite = deque(sorted(file_priorite, key=lambda m: m.arbitration_id))
            msg = file_priorite.popleft()

            nom, signaux = decoder_msg(msg.data, msg.arbitration_id)

            if nom == "capteur_temperature":
                temp = signaux["temperature"]
                print(f"[ECU] Température: {temp}°C")
                if temp > 95:
                    try:
                        data = encoder_msg("actionneur_ventilateur", {"ven_active": 1})
                        bus.send(can.Message(arbitration_id=0x200, data=data, is_extended_id=False))
                    except CanError:
                        print("[ECU]  Erreur envoi ventilateur")

            elif nom == "capteur_vitesse":
                vit = signaux["vitesse"]
                print(f"[ECU] Vitesse: {vit} km/h")
                if vit > 130:
                    try:
                        data = encoder_msg("actionneur_mturbo", {"turbo_active": 1})
                        bus.send(can.Message(arbitration_id=0x201, data=data, is_extended_id=False))
                    except CanError:
                        print("[ECU]  Erreur envoi moteur")

            elif nom == "capteur_pression":
                pres = signaux["pression"]
                print(f"[ECU] Pression: {pres} psi")

except KeyboardInterrupt:
    print("ECU STOP")
finally:
    bus.shutdown()
