def card_mask(number: str) -> str:
    """Принимает номер карты и возвращает ее маску"""
    list_digit = []
    symbols = number.split()
    for i in symbols:
        if i.isdigit() and len(i) == 16:
            list_digit.append(i)
            list_cleaned_digit = " ".join(list_digit)
            update_digit_card = (
                list_cleaned_digit[:4]
                + " "
                + list_cleaned_digit[4:6]
                + (len(list_cleaned_digit[6:8]) * "*")
                + " "
                + (len(list_cleaned_digit[8:12]) * "*")
                + " "
                + list_cleaned_digit[-4:]
            )
    return update_digit_card


def account_mask(number: str) -> str:
    """Принимает номер счета и возвращает его маску"""
    list_digit = []
    symbols = number.split()
    for i in symbols:
        if i.isdigit() and len(i) == 20:
            list_digit.append(i)
            update_digit_account = (len(number[-6:-4]) * "*") + number[-4:]
    return update_digit_account
