from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "input.txt"
INPUT = open(INPUT_FILE).readlines()

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

map_ = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN,
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}
"Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock"


def compute(input_):
    total = 0
    for i in input_:
        opponent, outcome = map_.get(i.split()[0]), map_.get(i.split()[1])
        total += outcome
        if outcome == DRAW:
            total += opponent
        elif outcome == WIN:
            total += winning_hand(opponent)
        elif outcome == LOSS:
            total += losing_hand(opponent)

    return total


def winning_hand(opponent: int) -> int:
    if opponent == ROCK:
        return PAPER
    if opponent == PAPER:
        return SCISSORS
    if opponent == SCISSORS:
        return ROCK


def losing_hand(opponent: int) -> int:
    if opponent == ROCK:
        return SCISSORS
    if opponent == PAPER:
        return ROCK
    if opponent == SCISSORS:
        return PAPER


if __name__ == "__main__":
    print(compute(INPUT))
    # 14069
