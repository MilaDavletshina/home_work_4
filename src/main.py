from widget import datetime_str, name_card
from processing import get_dict


if __name__ == "__main__":
    number = input()
    print(name_card(number))

    print(datetime_str("2018-07-11T02:26:18.671407"))

    print(
        get_dict(
            list,
        )
    )
