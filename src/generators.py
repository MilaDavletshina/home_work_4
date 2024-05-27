# функция, которая принимает список словарей с банковскими операциями
# (или объект-генератор, который выдает по одной банковской операции)
# и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
#
# Пример вызова функции:
#
def filter_by_currency(transactions, "USD"):
    with open("transactions.txt") as file:


usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions)["id"])
# Пример вывода:
#
# 939719570
# 142264268