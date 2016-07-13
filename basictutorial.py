def calculate(operator=None, *args):
    if operator == "add":
        total = 0 #starts out at zero and adds or subtracts

        for addends in args:
            total += addends

    elif operator == "multiply":
        total = 1 #starts at 1 because the beginning value has to be the first number in args

        for factors in args:
            total = total * factors

    elif operator == "subtract" or operator == "divide":
        total = args[0] #Makes the total number the first number given and is then manipulated

        if operator == "subtract":
            for subtrahends in args[1:]:
                total -= subtrahends

        if operator == "divide":
            for dividends in args[1:]:
                total = total / dividends

    elif operator == None:
        print("You didn't enter anything!")
        calculator()

    else:
        print(operator)
        print(args)
        print("You must have entered the wrong information.  Please try again. \n\n")
        calculator()

    return total

def calculator():
    operator = input("What would you like to do?  ").lower().strip()
    numbers = input("Which numbers would you like to {}?  ".format(operator))

    numbers = [int(x.strip()) for x in numbers.split(",")]

    print("If you {} {} by {} it equals: ".format(operator, numbers[0], tuple(numbers[1:])), calculate(operator, *numbers))


# Examples:
calculate("add", 2, 4)
calculate("subtract", 78, 8)
calculate("multiply", 3, 2)
calculate("divide", 6, 2)

print()

calculator()
