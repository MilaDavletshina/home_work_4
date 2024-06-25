from utils import get_finance_transaction
from transactions import read_transaction_csv, read_transaction_xlsx
from processing import get_dict, get_sort_dict
from filter import get_list_of_dict
from widget import name_card, datetime_str
from generators import filter_by_currency


def main() -> None:
    filter_by_selection = []  # отфильтрованный список пользователя

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print()
    while True:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )
        menu_item = input("Введите выбранный пункт меню: ")
        print()

        if menu_item == "1":
            print("Для обработки выбран JSON-файл")
            list_transaction = get_finance_transaction("data/operations.json")
            filter_by_selection.append(("format_json", "JSON"))
            break
        elif menu_item == "2":
            print("Для обработки выбран CSV-файл")
            print()
            list_transaction = read_transaction_csv("data/transactions.csv")
            filter_by_selection.append(("format_csv", "CSV"))
            break
        elif menu_item == "3":
            print("Для обработки выбран XLSX-файл")
            print()
            list_transaction = read_transaction_xlsx("data/transactions_excel.xlsx")
            filter_by_selection.append(("format_excel", "EXCEL"))
            break
        else:
            print("Не правильно! Попробуйте еще раз")
            print()
            continue

    while True:
        print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING 
        """
        )
        status = input("Введите выбранный статус: ").upper()
        print()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            filter_by_selection.append(("status", status))
            break
        else:
            print(f"Статус операции {status} недоступен")
            continue

    while True:
        sort_by_data = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_by_data == "да":
            sort_metod = input(
                "Отсортировать по возрастанию или по убыванию?: "
            ).lower()
            if sort_metod == "по возрастанию":
                filter_by_selection.append(("date", False))
                break
            elif sort_metod == "по убыванию":
                filter_by_selection.append(("date", True))
                break
        elif sort_by_data == "нет":
            break
        else:
            print("Некорректный ввод. Введите еще раз")
            continue

    while True:
        sort_by_transactions = input(
            "Выводить только рублевые тразакции? Да/Нет: "
        ).lower()
        if sort_by_transactions == "да":
            if menu_item == "1":
                filter_by_selection.append(("currency", "RUB"))
            else:
                filter_by_selection.append(("currency_code", "RUB"))
            break
        elif sort_by_transactions == "нет":
            break
        else:
            print("Некорректный ввод. Введите еще раз")
            continue

    while True:
        sort_by_word = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
        ).lower()
        if sort_by_word == "да":
            search_word = input("Введите слово для фильтрации: ")
            filter_by_selection.append(("description", search_word))
            break
        elif sort_by_word == "нет":
            break
        else:
            print("Некорректный ввод. Введите еще раз")
            continue

    transaction = list_transaction

    for key, value in filter_by_selection:
        if key == "status":
            transaction = get_dict(transaction, value)
        elif key == "date":
            transaction = get_sort_dict(transaction, value)
        elif key == "description":
            transaction = get_list_of_dict(transaction, value)
        elif key == "currency":
            transaction = filter_by_currency(transaction, value)
        elif key == "currency_code":
            transaction = [
                item for item in transaction if item["currency_code"] == value
            ]

    print("Распечатываю итоговый список транзакций...")

    if not transaction:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transaction)}")

    for key, value in filter_by_selection:
        if key == "format_json":
            for item in transaction:
                from_card = name_card((item["from"]))
                to_card = name_card((item["to"]))
                date = datetime_str(item["date"])
                description = item["description"]
                amount = item["operationAmount"]["amount"]
                currency = item["operationAmount"]["currency"]["name"]

        elif key == "format_csv":
            for item in transaction:
                from_card = name_card((item["from"]))
                to_card = name_card((item["to"]))
                date = datetime_str(item["date"])
                description = item["description"]
                amount = item["amount"]
                currency = item["currency_code"]

        elif key == "format_excel":
            for item in transaction:
                from_card = name_card((item["from"]))
                to_card = name_card((item["to"]))
                date = datetime_str(item["date"])
                description = item["description"]
                amount = item["amount"]
                currency = item["currency_code"]

        if description == "Открытие вклада":
            print(f"{date} {description}\n{to_card}\nСумма: {amount} {currency}")
        else:
            print(
                f"{date} {description}\n{from_card} -> {to_card}\nСумма: {amount} {currency}"
            )


if __name__ == "__main__":
    main()
