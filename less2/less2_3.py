"""3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:"""

import yaml


def write_dict_to_yaml(dict, file):
    with open(file, 'w', encoding="utf-8") as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode = True)

    with open(file, encoding="utf-8") as f_n:
        f_n_content = yaml.load(f_n)

    print(f_n_content == dict)


if __name__ == "__main__":
    my_dict = {
        '1265€': [1, 2, 3, 4],
        '222$': 8000,
        '300!': {
            'first': [1,2,3,4],
            'second': 800,
        }
    }

    write_dict_to_yaml(my_dict, 'file.yaml')
