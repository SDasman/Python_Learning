def duplicate_count(text):
    amtofduplicates = 0
    text = text.lower()
    textList = []
    doneduplicates = []
    for item in text:
        for letter in textList:
            if (letter == item) & (letter not in doneduplicates):
                amtofduplicates += 1
                doneduplicates.append(letter)
        textList.append(item)
    return amtofduplicates
print(duplicate_count("inaAdivisibility"))