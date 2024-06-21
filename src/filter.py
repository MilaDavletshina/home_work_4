# Напишите функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
# а возвращать список словарей, у которых в описании есть данная строка. При реализации этой функции можно
# использовать библиотеку re для работы с регулярными выражениями.

import re
from utils import get_finance_transaction


def get_list_of_dict(list_transaction, search_bar):
    new_list_dict = []
    for transaction in list_transaction:
        if "description" in transaction and re.search(search_bar, transaction["description"], flags=re.IGNORECASE):
            new_list_dict.append(transaction)
    return new_list_dict


search_bar = input("Введите банковскую операцию: ")
list_transaction = get_finance_transaction("data/operations.json")

print(get_list_of_dict(list_transaction, search_bar))
