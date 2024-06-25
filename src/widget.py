from datetime import datetime

from masks import account_mask, card_mask
from utils import get_finance_transaction


def name_card(number: str) -> str:
    """Принимает информацию — тип карты/счета и номер карты/счета и возвращает тип карты и маску карты/счета"""
    list_alpha = []
    symbols = number.split()
    for i in symbols:
        if i.isalpha():
            list_alpha.append(i)
            list_cleaned_alpha = " ".join(list_alpha)

    if ("Счет" in list_cleaned_alpha) or (
        "счет" in list_cleaned_alpha
    ):  # Добавляем маску
        return list_cleaned_alpha + " " + account_mask(number)
    else:
        return list_cleaned_alpha + " " + card_mask(number)


# number = input("Введите данные: ")
# print(name_card(number))


def datetime_str(name: str) -> str:
    """Принимает строку и возвращает строку с датой"""
    # date_obj = datetime.strptime(name, "%Y-%m-%dt%H:%M:%S.%f")
    # return date_obj.strftime("%d.%m.%Y")
    return str(datetime.strptime(name.split("T")[0], "%Y-%m-%d").strftime("%d.%m.%Y"))


# print(datetime_str("2018-07-11T02:26:18.671407"))


# if __name__ == "__main__":
#     list_transaction = get_finance_transaction("data/operations.json")
#     transaction = list_transaction
#     for item in transaction:
#         if "from" in item:
#             from_card = name_card((item["from"]))
#             print(from_card)
