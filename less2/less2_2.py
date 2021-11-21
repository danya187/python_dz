"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding="utf-8") as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w', encoding="utf-8") as f_w:
        json.dump(dict_to_json, f_w, indent=4,ensure_ascii=False)


if __name__ == "__main__":
    write_order_to_json('Банан', 68, 986, 'Vitalya', '21.11.2021')
    write_order_to_json('Яблоко', 52, 700, 'Pushkin', '21.11.2021')
    write_order_to_json('Апельсин', 3, 1200, 'Petr', '21.11.2021')
    write_order_to_json('Груша', 9, 500, 'Alex', '21.11.2021')
