from typing import Iterable
from typing import Any

def get_dict(name_dict: Any, value: Iterable[str] = "EXECUTED") -> str:
    """Функция возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение"""
    new_dict = []
    for i in name_dict:
        if i["state"] == value:
            new_dict.append(i)
    return new_dict


def get_sort_dict(name_dict: Any, ascending=True) -> str:
    """Функция сортирует по убыванию даты. Второй аргумент необязательный, задает порядок сортировки"""
    return sorted(name_dict, key=lambda x: x.get("date", 0), reverse=ascending)
