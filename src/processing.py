from typing import Iterable


def get_dict(name_dict: Iterable, value: Iterable[str] = "EXECUTED") -> str:
    """Функция возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение"""
    new_dict = []
    for i in name_dict:
        if i.get("state") == value:
            new_dict.append(i)
    return new_dict


# name_dict = [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#              {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#              {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#              {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},]
# print(get_dict(name_dict,))


def get_sort_dict(name_dict: Iterable, ascending=True) -> str:
    """Функция сортирует по убыванию даты. Второй аргумент необязательный, задает порядок сортировки"""
    return sorted(name_dict, key=lambda x: x.get("date", 0), reverse=ascending)


# print(
#         get_sort_dict(
#             [
#                 {
#                     "id": 41428829,
#                     "state": "EXECUTED",
#                     "date": "2019-07-03T18:35:29.512364",
#                 },
#                 {
#                     "id": 939719570,
#                     "state": "EXECUTED",
#                     "date": "2018-06-30T02:08:58.425572",
#                 },
#                 {
#                     "id": 594226727,
#                     "state": "CANCELED",
#                     "date": "2018-09-12T21:27:25.241689",
#                 },
#                 {
#                     "id": 615064591,
#                     "state": "CANCELED",
#                     "date": "2018-10-14T08:21:33.419441",
#                 },
#             ]
#         ),
#     )
