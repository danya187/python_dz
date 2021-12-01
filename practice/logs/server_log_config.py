
import logging.handlers
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.const import LOGGING_LVL

SERVER_FORMATTER = logging.Formatter('%(asctime)-15s %(levelname)-10s %(filename)-12s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)


if __name__ == '__main__':
    LOGGER.critical('Критичсекая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная инфомрация')
    LOGGER.info('Информационное сообщение')

