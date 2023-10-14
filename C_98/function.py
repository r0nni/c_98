
def countWords():

    fileName = input("Enter the name of your file: ")

    numb=0

    file= open(fileName, 'r')
    for words in file:
        line = words.split()
        numb=numb+len(line)
    print("Numbers of words:")
    print(numb)
    
countWords()