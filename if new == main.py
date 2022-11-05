def hello():
    print("hello!")


if __name__ == "__main__":
    hello()
    print("running module directly")
else:
    print("running module indirectly")

# why this statement is used?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# python interpreter sets "special variables", one of which is __name__
# then python will execute the code found within __main__
