def fileinfo():
    words = 0
    with open("story.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            words = words + len(line.split())

        print("Total no of words are: ",words)

fileinfo()
    