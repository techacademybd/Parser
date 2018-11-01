from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()*100

text1 = open("Sample1.txt")
text2 = open("Sample2.txt")

text1 = text1.read()
text2 = text2.read()


def removeSpaces(text):
    text = text.split()
    output = ""
    for t in text:
        output += t
    return output

text1 = removeSpaces(text1)

text2 = removeSpaces(text2)

print("%i%%" % (similar(text1, text2)))
