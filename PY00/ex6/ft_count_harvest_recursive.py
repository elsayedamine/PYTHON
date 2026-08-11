def recursion(start, stop):
    if (start > stop):
        return 
    print("Day ", start)
    recursion(start + 1, stop)


def ft_count_harvest_recursive():
    time = input("Days until harvest: ")
    recursion(1, int(time))
    print("Harvest time!")