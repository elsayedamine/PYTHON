def my_range(start=0, stop=None, step=1):
    # this is for distinguishig whether the stop was provided wla la
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("range(): step must not be zero")

    if step > 0:
        # those 3 lines are the main idea
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


if __name__ == "__main__":
    for i in my_range(10):
        print(i)
