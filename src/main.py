
# from src.generators import (
#     card_number_generator,
#     filter_by_currency,
#     transaction_descriptions,
# )
# from src.processing import get_dict, get_sort_dict
# from widget import datetime_str, name_card
from masks import card_mask
# from src.decorators import log
# from utils import (get_finance_transaction, get_transaction_amount)




if __name__ == "__main__":
    # Принимает номер карты и возвращает ее маску
    number = input("Введите номер: ")
    print(card_mask(number))

    # Принимает информацию — тип карты/счета и номер карты/счета и возвращает тип карты и маску карты/счета
    # number = input("Введите данные: ")
    # print(name_card(number))
    #
    # # Принимает строку и возвращает строку с датой
    # print(datetime_str("2018-07-11T02:26:18.671407"))
    #
    # # Возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию знач.
    # name_dict = [
    #     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]
    # print(
    #     get_dict(
    #         name_dict,
    #     )
    # )
    #
    # # Сортирует по убыванию даты
    # print(
    #     get_sort_dict(
    #         [
    #             {
    #                 "id": 41428829,
    #                 "state": "EXECUTED",
    #                 "date": "2019-07-03T18:35:29.512364",
    #             },
    #             {
    #                 "id": 939719570,
    #                 "state": "EXECUTED",
    #                 "date": "2018-06-30T02:08:58.425572",
    #             },
    #             {
    #                 "id": 594226727,
    #                 "state": "CANCELED",
    #                 "date": "2018-09-12T21:27:25.241689",
    #             },
    #             {
    #                 "id": 615064591,
    #                 "state": "CANCELED",
    #                 "date": "2018-10-14T08:21:33.419441",
    #             },
    #         ]
    #     ),
    # )
    #
    # # Принимает список словарей с банковскими операциями и возвращает итератор
    # transactions = [
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {
    #             "amount": "9824.07",
    #             "currency": {"name": "USD", "code": "USD"},
    #         },
    #         "description": "Перевод организации",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702",
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {
    #             "amount": "79114.93",
    #             "currency": {"name": "USD", "code": "USD"},
    #         },
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    #     },
    #     {
    #         "id": 873106923,
    #         "state": "EXECUTED",
    #         "date": "2019-03-23T01:09:46.296404",
    #         "operationAmount": {
    #             "amount": "43318.34",
    #             "currency": {"name": "руб.", "code": "RUB"},
    #         },
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 44812258784861134719",
    #         "to": "Счет 74489636417521191160",
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {
    #             "amount": "56883.54",
    #             "currency": {"name": "USD", "code": "USD"},
    #         },
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #         "operationAmount": {
    #             "amount": "67314.70",
    #             "currency": {"name": "руб.", "code": "RUB"},
    #         },
    #         "description": "Перевод организации",
    #         "from": "Visa Platinum 1246377376343588",
    #         "to": "Счет 14211924144426031657",
    #     },
    # ]
    # usd_transactions = filter_by_currency(transactions, "RUB")
    #
    # for _ in range(2):
    #     print(next(usd_transactions)["id"])
    #
    # # Принимает список словарей и возвращает описание каждой операции по очереди
    # descriptions = transaction_descriptions(transactions)
    #
    # for _ in range(5):
    #     print(next(descriptions))
    #
    # # Генерирует номера карт в формате XXXX XXXX XXXX XXXX
    # for card_number in card_number_generator(1, 5):
    #     print(card_number)
    #
    # # Декоратор
    # @log(filename="mylog.txt")
    # def my_function(x, y):
    #     return x + y
    #
    # my_function(1, 2)

    # # Принимает json файл и возвращает список словарей о финансовых транзакциях
    # print(get_finance_transaction("data/operations.json"))

    # # Принимает транзакцию и возвращает сумму в рублях
    # transaction = {"amount": "200", "currency": "USD"}
    # amount = get_transaction_amount(transaction)
    # print(amount)
