from typing import Iterable


def get_dict(list: str, value: Iterable[str] = "EXECUTED") -> str:
    """Функция возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение"""
    new_dict = []
    for i in list:
        if i["state"] == value:
            new_dict.append(i)
    return new_dict


def get_sort_dict(list: str, ascending: bool = True) -> str:
    """Функция сортирует по убыванию даты. Второй аргумент необязательный, задает порядок сортировки"""
    return sorted(list, key=lambda x: x.get("date", 0), reverse=ascending)
