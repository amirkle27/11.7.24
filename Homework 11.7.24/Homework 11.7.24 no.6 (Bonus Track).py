#Start
word1: str = str(input("Enter your 1st word please"));
word2: str = str(input("Enter your 2nd word please"));
while word1 != word2:
    if word1 == word2:
        print(word1, word2)
        break;
    else:
        wordx: str = (word1+ " " + word2)
        while word1!=word2:
            word1: str = str(input("Enter your 1st word please"));
            word2: str = str(input("Enter your 2nd word please"));
            wordx: str = (wordx+ " " + word1 + " " + word2)
            wordy: str = (wordx)
            if word1 == word2:
              print(wordy)
              break;
#End

