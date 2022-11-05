# exception - events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You cannot divide by zero... moron!")
except ValueError:
    print("You cannot divide number with letters... moron!")
except Exception:
    print("Something went wrong...")
else:
    print(result)   # it is better to use in else statement because it prevents executing other blocks of code
