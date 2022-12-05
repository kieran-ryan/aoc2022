import re
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).read()


def compute(input_):
    stacks = []
    instructions = []

    # Split stacks from instructions
    lines = input_.splitlines()
    for line in lines:
        if line.startswith("move"):
            numbers = re.findall(r"\d+", line)
            instructions.append(numbers)
        elif line:
            stacks.append(list(line[1:-1][::4]))

    # Create stacks dictionary
    index = stacks.pop()
    stacks_dict = {i: [] for i in index}

    # Populate stacks dictionary
    for line in stacks:
        for index, char in enumerate(line):
            if char := char.strip():
                stacks_dict[str(index + 1)].insert(0, char)

    # Pop a number of values from one stack and push to another
    for instruction in instructions:
        num, origin, destination = instruction
        for i in range(int(num)):
            val = stacks_dict[origin].pop()
            stacks_dict[destination].append(val)

    return "".join([stacks_dict[key][-1] for key in stacks_dict.keys()])


if __name__ == "__main__":
    print(compute(INPUT))
    # 'JCMHLVGMG'
