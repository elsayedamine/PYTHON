import sys


class InvalidInput(Exception):
    def __init__(self, message: str = "No scores provided. Usage: python3 \
                 ft_score_analytics.py <score1> <score2> ..."):
        super().__init__(message)


def validator(argv: list[str]) -> list[int]:
    if (len(argv) == 1):
        raise InvalidInput()
    scores: list[int] = []
    for arg in argv:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if (len(scores) == 0):
        raise InvalidInput()
    return scores


def analyzer(scores: list[int]):
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main():
    print("=== Player Score Analytics ===")
    try:
        scores: list[int] = validator(sys.argv[1:])
        analyzer(scores)
    except InvalidInput as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
