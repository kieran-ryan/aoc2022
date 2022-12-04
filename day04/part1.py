from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).readlines()


def compute(input_):
    total = 0
    for line in input_:
        first, second = line.split(",")

        f1, f2 = first.split("-")
        s1, s2 = second.split("-")

        first_range = set(range(int(f1), int(f2) + 1))
        second_range = set(range(int(s1), int(s2) + 1))

        total += int(
            first_range.issubset(
                second_range) or first_range.issuperset(second_range)
        )
    return total


if __name__ == "__main__":
    print(compute(INPUT))
    # 487
