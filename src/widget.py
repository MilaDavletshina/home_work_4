from datetime import datetime
from src.masks import account_mask, card_mask


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


def datetime_str(name: str) -> str:
    """Принимает строку и возвращает строку с датой"""
    date_obj = datetime.strptime(name, "%Y-%m-%dt%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
