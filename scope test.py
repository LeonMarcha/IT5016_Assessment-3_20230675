a = 10
b = 20
c = 0


def _sum():
    global c

    c = a + b
    return a + b


print(c)
print(_sum())

# now works due to global
