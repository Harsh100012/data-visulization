try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Numbers are valid!")
except ValueError:
    print("Numbers are not valid!")
