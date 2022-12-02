from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).read()


def compute(input_: str) -> int:
    as_str = [elf.split() for elf in input_.split("\n\n")]
    as_int = [[int(calorie) for calorie in elf] for elf in as_str]
    return max(sum(elf) for elf in as_int)


if __name__ == "__main__":
    print(compute(INPUT))
    # 70296
