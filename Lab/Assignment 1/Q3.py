def fileinfo():
    uppercase = 0
    with open("story.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            for char in line:
              if(char.isupper()):
                uppercase = uppercase + 1

        print("Total no of uppercase are: ",uppercase)

fileinfo()
    