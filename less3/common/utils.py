import json
from common.const import MAX_PACKAGE_LENGTH, ENCODING




def get_message(client):
    encoded_responce = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_responce, bytes):
        json_response = encoded_responce.decode(ENCODING)
        responce = json.loads(json_response)
        if isinstance(responce, dict):
            return responce
        raise ValueError
    raise ValueError


def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)