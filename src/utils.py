import json


def get_finance_transaction(input_file):
    """ Функция принимает json файл и возвращает список словарей о финансовых транзакциях"""
    try:
        with open(input_file) as file:
            operations = json.load(file)
            return operations
    except:
        return []




