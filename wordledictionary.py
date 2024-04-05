import re
from english_words import get_english_words_set
from PyDictionary import PyDictionary as dict

continueQ = True


print("Welcome to Wordle Word Finder!")

while continueQ == True:
    ###Attempt a for loop instead
    regexString = ["'","\w","\w","\w","\w","\w","'"]
    listBlanks = ["_","_","_","_","_"]
    mustLetters = []

    for i in range(1,6):
        letter = input("Please enter the letter for blank "+ str(i) +". If you dont know please press enter: " )
        if letter == "":
            nonLetter = input("Since you dont know the letter, do you know any letter(s) in the word that do(es) NOT belong in this space? \nPlease type them one after another no spaces or hit enter: ")
            if nonLetter != "":
                regexString[i] = "[^" + nonLetter +"]"
                mustLetters = mustLetters + list(nonLetter)
            print(''.join(listBlanks)+"\n")
        else:
            listBlanks[i-1] = letter
            regexString[i] = letter
            print(''.join(listBlanks)+"\n")

    ##Actually regex search
    regexInput = ''.join(regexString)
    strong = str(get_english_words_set(['gcide'], lower=True))
    searchWord = re.findall(regexInput, strong)


    def run_list(searchWord, mustLetters):
        finalList = []
        trues = 0
        ### first remove duplicates in the list
        mustLetters = list(set(mustLetters))
        ### Actually run through results
        for i in searchWord:
            for e in mustLetters:
                if e in i:
                    trues += 1
            if trues == len(mustLetters):
                finalList.append(i)
            trues = 0
        return finalList

    print("Your final word list is: ")
    print(run_list(searchWord, mustLetters))

    ## Further narrow down options
    narrowOpt = input("Would you like to further narrow down your options? Y/N ")
    if narrowOpt.lower() == "y":
        otherLetters = input("List all letters that Must be in the word: ")
        if otherLetters != "":
            mustLetters = mustLetters + list(otherLetters)
        print(run_list(searchWord,mustLetters))

    ## Do you want to continue?
    continueQuestion = input("Would you like to go again? Y/N \n")

    if continueQuestion.lower() == "y":
        continueQ = True
    else:
        continueQ = False

