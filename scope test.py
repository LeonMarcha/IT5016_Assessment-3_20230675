a = 10
b = 20
c = 0

def _sum():
    c = a + b
    return a + b


print(c)
print(_sum())

# error still because c inside function is separate from c outside
