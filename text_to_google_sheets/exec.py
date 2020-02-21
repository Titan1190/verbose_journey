import string
import csv

# Prompts user for input text
text = input("\nPlease input text: ")

# Data to list seperated by space
text = text.lower().split()
print("Testing text: {}".format(text))


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# Help function
def help():
    print("""
    Your options Mosier ~
    HELP - displays all commands & descriptions
    EXIT - exits the console
    ABC - alphabetizes text & converts to lexicographically ordered spreadsheet
    """)


# ABC function
def abc(text):

    text.sort()
    text = [a.strip(' ') for a in text]
    letterList = list(string.ascii_lowercase[:25])
    var = 0
    sortedText = []
    array = []

    # Creates a nested list with each word in ABC, all A's in first list element, all B's in second, etc.

    for word in text:
        success = False
        while not success:
            if (word[0] == letterList[var]):
                array.append(letterList[var])
                array.append(word)
                success = True
            else:
                sortedText.append(array[:])
                array.clear()
                var +=1

    with open('C:/Users/Bikeh/OneDrive/Desktop/csv_files/text.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = letterList)

        writer.writeheader()
        for i in range(0,2*len(max(sortedText, key=len)),2):
            for text in sortedText:
                if len(text) > i:
                    array.append(text[i])
                    array.append(text[i+1])
            dictSortedText = Convert(array)
            array.clear()
            writer.writerow(dictSortedText)

# Creates user interface
while True:
    consoleInput = input("> ")

    if consoleInput == "EXIT":
        break

    elif consoleInput == "HELP":
        help()

    elif consoleInput == "ABC":
        abc(text)

    else:
        print("\nSorry my good sir, but that is not a valid command. May I suggest the 'HELP' option if needed?")
