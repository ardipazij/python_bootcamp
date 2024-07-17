from typing import Dict


def add_ingot(parse: Dict[str, int]) -> Dict[str, int]:
    new_parse = parse.copy()
    if "gold ignot" not in new_parse:
        new_parse["gold ignot"] = 1
    else:
        new_parse["gold ignot"] += 1
    return new_parse


def get_ingot(parse: Dict[str, int]) -> Dict[str, int]:
    new_parse = parse.copy()
    if "gold ignot" in new_parse and new_parse["gold ignot"] > 0:
        new_parse["gold ignot"] -= 1
    return new_parse


def empty(parse) -> Dict[str, int]:
    return {}


def main():
    purse = {"Hello": 2}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))


if __name__ == "__main__":
    main()
