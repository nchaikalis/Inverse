"""
Find the inverse of a number using the Euclidean extended algorithm
"""


# Euclidean extended algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        d, x, y = egcd(b % a, a)
        return d, y - (b // a) * x, x


while True:
    try:
        a = input('Give the order: ')
        a = int(a)
        b = input('Give the number in order to find the inverse of that number: ')
        b = int(b)
        break
    except ValueError:
        print("Wrong input!")

d, x, y = egcd(a, b)
print("%d = %d*(%d) + %d*(%d)\nThe inverse number of: %d is the number: %d." % (d, a, x, b, y, b, y))
