def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

for x in zero_to_infinity():
    print(x)