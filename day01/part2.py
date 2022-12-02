from part1 import INPUT


def compute(input_: str) -> int:
    as_str = [elf.split() for elf in input_.split("\n\n")]
    as_int = [[int(calorie) for calorie in elf] for elf in as_str]
    return sum(sorted(sum(elf) for elf in as_int)[-3:])


if __name__ == "__main__":
    print(compute(INPUT))
    # 205381
