from my_range import my_range


def my_for(iterable, function):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            function(value)
        except StopIteration:
            break


if __name__ == "__main__":
    my_for([i for i in my_range(10, 0, -1)], print)
