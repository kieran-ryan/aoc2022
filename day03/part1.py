from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).readlines()


def compute(input_):
    total = 0
    for rucksack in input_:
        r = rucksack.strip()
        compartment1, compartment2 = r[: len(r) // 2], r[len(r) // 2:]
        common_item_type = set(compartment2).intersection(compartment1).pop()
        total += priority(common_item_type)
    return total


def priority(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


if __name__ == "__main__":
    print(compute(INPUT))
    # 8240
