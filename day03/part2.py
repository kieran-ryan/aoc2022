from pathlib import Path

from part1 import priority

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).read()


def compute(input_):
    total = 0
    index1, index3 = 0, 3
    for group in range(len(input_.splitlines()) // 3):
        one, two, three = input_.splitlines()[index1:index3]
        total += priority(set(one).intersection(
            set(two)
        ).intersection(three).pop())
        index1 += 3
        index3 += 3
    return total


if __name__ == "__main__":
    print(compute(INPUT))
    # 2587
