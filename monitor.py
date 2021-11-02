import requests
import sys
import re

from bs4 import BeautifulSoup as BS


def get_data_from_hotgame(url: str) -> None:
    """Обращается к сайту hot-games.info
    Парсит HTML, находит нужную строчку с ценой,
    печатает её в консоль"""
    print(url, end=" - ")
    response = requests.get(url)
    if str(response.status_code) == "404":
        print("Game not found")

    elif str(response.status_code) == "200":
        soup = BS(response.text, "html.parser")
        data = soup.findAll('span', class_="price-value")
        pattern = (r'data-final_price="(\d)*(\.)?(\d)*"')
        result = re.search(pattern, str(data[0]))
        print(result.group(0))

    else:
        print(f"Статус ответа: {response.status_code}")


def make_an_url(name: str, mode: str) -> None:
    """Создаёт корректную ссылку на хотгейм"""
    names = name.split(" ")
    if mode == "input":
        for index, _ in enumerate(names):
            names[index] = _.capitalize()
    url = f"https://hot-game.info/game/{'-'.join(names)}"
    get_data_from_hotgame(url)


def request_caller_for_lists(data: list[str]) -> None:
    """Для режима text. Вызывает функцию
    get_data_from_hotgame для каждой ссылки списка"""
    for url in data:
        get_data_from_hotgame(url)


def get_name(mode: str = "input") -> None:
    """Вызывает функции создания url в зависимости от режима
    Режим input предлагает ввод названия через консоль
    Режим text читает названия из файла games.txt
    Режим manual повторяет input для случаев, когда название
    в ссылке используется с маленькой буквы"""
    if mode == "input" or mode == "manual":
        print("Введите название")
        name = input()
        make_an_url(name, mode)

    elif mode == "text":
        with open('games.txt', 'r') as file:
            data = file.read().splitlines()
        request_caller_for_lists(data)

    else:
        print("Доступные режимы - text - manual")


def mode_selector() -> None:
    """Вызывает get_name, передавая туда название
    режима из консоли. Если режима нет, просто вызывает
    get_name()
    Режимы: text, manual и input"""
    try:
        mode = sys.argv[1]
        get_name(mode)
    except IndexError:
        get_name()


mode_selector()
