from masks import card_mask, account_mask


def name_card(number: str) -> str:
    """Принимает информацию — тип карты и номер карты и возвращает тип карты"""
    list_alpha = []
    symbols = number.split()
    for i in symbols:
        if i.isalpha():
            list_alpha.append(i)
            list_cleaned_alpha = " ".join(list_alpha)

    if "Счет" in list_cleaned_alpha:
        return list_cleaned_alpha + " " + account_mask(number)
    else:
        return list_cleaned_alpha + " " + card_mask(number)


from datetime import datetime


def datetime_str(name: str) -> str:
    """Принимает строку и возвращает строку с датой"""
    date_obj = datetime.strptime(name, "%Y-%m-%dt%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
