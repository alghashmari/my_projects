def add(*args):
    for total in args:
        total = sum(args)
        return total


print(add(1,5,8,9,9,4,85,1,5,5,5))
