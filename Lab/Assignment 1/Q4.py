def fileinfo():
    words = 0
    with open("story.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
              if(len(word) < 4):
                 print(word, end=" ")

fileinfo()


