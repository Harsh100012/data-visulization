try:
    with open("abc.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("File not found")
