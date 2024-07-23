#Question 1
print("Linre 1")
print("Linre 2")
print("Linre 3")
print("Linre 4")
try: 
    print(100/0)
    open("abc.txt")
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError:
    print("file does not found")
print("Linre 5")
print("Linre 6")
print("Linre 7")
print("Linre 8")