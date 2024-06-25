import re
from utils import get_finance_transaction

def get_list_of_dict(list_transaction, search_bar):
    """Функция возращает список словарей по заданной пользователем операции"""
    new_list_dict = []
    for transaction in list_transaction:
        if "description" in transaction and re.search(
            search_bar, transaction["description"], flags=re.IGNORECASE
        ):
            new_list_dict.append(transaction)
    return new_list_dict

# search_bar = input("Введите банковскую операцию: ")
# list_transaction = get_finance_transaction("data/operations.json")
# print(get_list_of_dict(list_transaction, search_bar))

def get_list_of_dict_by_description(list_transaction: list, description: str) -> dict:
    """Функция возвращает колчество операций по заданной категории"""
    dict_by_description = {}
    count = 0
    for transaction in list_transaction:
        if "description" in transaction and re.search(description, transaction["description"], flags=re.IGNORECASE):
            count += 1
            dict_by_description[description] = count

    return dict_by_description

# description = input("Введите категорию банковской операции: ")
# list_transaction = get_finance_transaction("data/operations.json")
# print(get_list_of_dict_by_description(list_transaction, description))
