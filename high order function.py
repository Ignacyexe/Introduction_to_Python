# higher order functions - a function that either: accepts a function as an argument or return a function
# in python functions are also objects

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(fu):
    text = fu("Hello")
    print(text)


hello(loud)
hello(quiet)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


print()
divide = divisor(2)
print(divide(10))
