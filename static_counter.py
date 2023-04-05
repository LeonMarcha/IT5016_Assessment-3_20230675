# static counter from chat gpt
""" tried to add this code to my ticketing system, but it didn't work
the reason being; it was inserted into a class
"""


def static_counter():
    static_counter.count += 1
    return static_counter.count


static_counter.count = 2000

print(static_counter())
print(static_counter())

