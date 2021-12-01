import argparse
import socket
import sys
import json
import logging
import logs.server_log_config
from errors import IncorrectDataRecivedError
from common.const import ACTION, ACCOUNT_NAME,RESPONSE,MAX_CONNECTIONS,\
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT,DEFAULT_IP,RESPONDEFAULT_IP_ADDRESSE
from common.utils import get_message,send_message


SERVER_LOGGER = logging.getLogger('server')


def process_client_msg(message):

        SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
        if ACTIONS in message and message[ACTIONS] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {RESPONSE: 200}
        return {
            RESPONDEFAULT_IP_ADDRESSE: 400,
            ERROR: 'request error'
        }


def create_arg_parses():
    parses = argparse.ArgumentParses()
    parses.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parses.add_argument('-a', default='', nargs='?')
    return parses


def main():

        parses = create_arg_parses()
        namespace = parses.parse_args(sys.argv[1:])
        listen_address = namespace.a
        listen_port = namespace.p

        if not 1023 < listen_port < 65536:
            SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта'
                                   f'{listen_port}.Допустимые значения от 1024 до 65535.')
            sys.exit(1)
        SERVER_LOGGER.info(f'Запущен сервер, порт для подключений: {listen_port},'
                           f'адрес с которого принимаются сообщения : {listen_address}.'
                           f'Если адрес не указан, то принимаются соединения с любых адресов.')






        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        transport.bind((listen_address, listen_port))


        transport.listen(MAX_CONNECTIONS)

        while True:
            client, client_address = transport.accept()
            SERVER_LOGGER.info(f'Установлено соединение с устройством {listen_address}.')
            try:
                message_from_client = get_message(client)
                SERVER_LOGGER.debug(f'Получено сообщение:{message_from_client}.')
                response = process_client_msg(message_from_client)
                SERVER_LOGGER.info(f'Сформирован ответ клиенту: {response}.')
                send_message(client, response)
                SERVER_LOGGER.debug(f'Соединение с клиентом: {client_address} закрывается.')
                client.close()
            except json.JSONDecodeError:
                SERVER_LOGGER.error(f'Не удалось декодировать Json строку, полученную от '
                                    f'клиента: {client_address}. Соединение закрывается.')
                client.close()
            except IncorrectDataRecivedError:
                SERVER_LOGGER.error(f'От клиента: {client_address} приняты неккоректные данные.'
                                    f'Соединение закрывается.')
                client.close()


if __name__ == '__main__':
    main()
