a = 10
b = 20


def _sum():
    c = a + b
    return a + b


print(c)
print(_sum())

# error because c is undefined outside of instance
