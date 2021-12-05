import argparse
import socket
import time
import sys
import json
import logging
import logs.client_log_config
from errors import ReqFielMissingError
from common.const import ACTION, ACCOUNT_NAME,RESPONSE,MAX_CONNECTIONS,\
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT,DEFAULT_IP,RESPONDEFAULT_IP_ADDRESSE
from common.utils import get_message, send_message
from decos import log


CLIENT_LOGGER = logging.getLogger('Client')


@log
def create_presence(account_name = "Guest"):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}.')
    return out


@log
def process_ans(message):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}.')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ReqFielMissingError(RESPONSE)


@log
def create_arg_parses():

    parses = argparse.ArgumentParses()
    parses.add_argument('addr', default=DEFAULT_IP, type=int, nargs='?')
    parses.add_argument('port', default=DEFAULT_PORT, nargs='?')
    return parses


def main():

    parses = create_arg_parses()
    namespace = parses.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    if not 1023 < server_port < 65535:
        CLIENT_LOGGER.critical(f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
                               f'Допустимы адреса с 1023 до 65535. Клиент завершается.')
        sys.exit(1)

    CLIENT_LOGGER.info(f'запущен клиент с параметрами:'
                       f'адрес сервера: {server_address}, порт: {server_port}.')


    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = process_ans(get_message(transport))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}.')
        print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error(f'Не удалось закодировать полученную Json строку.')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port},'
                               f'конечный компьютер отверг запрос на подключение.')
    except ReqFielMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствуют необходимое поле'
                            f'{missing_error.missing_field}')



if __name__ == '__mian__':
    main()
