import cantools

# Charger le fichier .dbc une fois
db = cantools.database.load_file("dbc/vehicule.dbc")

def encoder_msg(message_name, signal_dict):
    return db.get_message_by_name(message_name).encode(signal_dict)

def decoder_msg(data, message_id):
    msg = db.get_message_by_frame_id(message_id)
    return msg.name, msg.decode(data)
