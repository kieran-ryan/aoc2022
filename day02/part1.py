from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).readlines()

ROCK = 1
PAPER = 2
SCISSORS = 3

map_ = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}


def compute(input_):
    total = 0
    for i in input_:
        opponent, user = map_.get(i.split()[0]), map_.get(i.split()[1])
        total += user
        if opponent == user:
            total += 3
        elif is_winner(user, opponent):
            total += 6
    return total


def is_winner(user: int, opponent: int) -> bool:
    if user == 1 and opponent == 3:
        return True
    if user == 2 and opponent == 1:
        return True
    if user == 3 and opponent == 2:
        return True
    return False


if __name__ == "__main__":
    print(compute(INPUT))
    # 14069
