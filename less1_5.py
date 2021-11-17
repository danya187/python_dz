import subprocess
import chardet

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_now in ARGS:

    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)

    i = 0

    for line in ping_process.stdout:

        if i < 10:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('_' * 30)
            break
