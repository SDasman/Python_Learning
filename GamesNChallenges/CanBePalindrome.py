
# Find out if a given string can be rearranged into a palindrome. To check if it is an exisiting palindrome - one knows to compare the reversed string to the original - the alternate question is can any string be a palindrome.

def canbepalindrome(text):
    from collections import Counter
    newtext = Counter(text)
    oddcount = 0 #Counts the number of odd letters in the string. Even letters mean that it is a palindrome with the exception of ONE odd letter.
    for value in [newtext[i] for i in newtext]:
        if value%2 == 1:
            oddcount += 1
    if oddcount > 1:
        return f'No {text} does not work!'
    else:
        return f'Yes {text} works!'

print(canbepalindrome('asdsdhhffaassdd'))
print(canbepalindrome('soahdgiupaegwibaspicubawe'))
print(canbepalindrome('aabaa'))
print(canbepalindrome('aba'))
print(canbepalindrome('aaaab'))
print(canbepalindrome('aabca'))
print(canbepalindrome('aabvcaa'))
print(canbepalindrome('paab'))
print(canbepalindrome('paabaap'))
