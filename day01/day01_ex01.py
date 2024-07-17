from typing import Dict, List


def split_booty(*purses: Dict[str, int]):
    total_gold_ingots = 0
    for purse in purses:
        total_gold_ingots += purse.get("gold_ingots", 0)
    gold_ingots_per_purse = total_gold_ingots // 3
    variance = total_gold_ingots % 3
    purse1 = {"gold_ingots": gold_ingots_per_purse}
    purse2 = {"gold_ingots": gold_ingots_per_purse}
    purse3 = {"gold_ingots": gold_ingots_per_purse}
    if variance > 0:
        purse1["gold_ingots"] += 1
    if variance > 1:
        purse2["gold_ingots"] += 1

    return purse1, purse2, purse3


def main():
    purses: List[Dict[str, int]] = [
        {"gold_ingots": 2},
        {"gold_ingots": 2},
        {"gold_ingots": 4},
        {"gold_ingots": 11},
        {"gold_ingots": 9},
        {"gold_ingots": 3},
        {"gold_ingots": 2},
        {"apples": 10},
    ]
    v1, v2, v3 = split_booty(purses[5], purses[6], purses[7])
    print(v1, v2, v3)


if __name__ == "__main__":
    main()
