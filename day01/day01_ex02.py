from typing import Dict
from day01_ex00 import add_ingot, get_ingot, empty


def signal(func: any) -> any:
    def wrapper(purse: Dict[str, int]) -> Dict[str, int]:
        print("SQUEAK")
        return func(purse)

    return wrapper


add_ingot = signal(add_ingot)
get_ingot = signal(get_ingot)
empty = signal(empty)


def main():
    purse = {"Hello": 2}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))


if __name__ == '__main__':
    main()
