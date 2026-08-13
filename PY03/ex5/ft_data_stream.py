import random


players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move",
           "climb", "swim", "release", "use"]


def gen_event():
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple[str, str]]):
    while events:
        index: int = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main():
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        val1, val2 = next(gen)
        # print(f"Event {i}: Player {str(val1)[1:-1]}
        # did action {"".join(val2)}")
        print(f"Event {i}: Player {val1} did action {val2}")
    events: list[tuple[str, str]] = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event} "
              f"Remaining events: {len(events)}")


if __name__ == "__main__":
    main()
