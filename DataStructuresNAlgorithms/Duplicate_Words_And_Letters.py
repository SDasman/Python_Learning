# Find duplicates in a list and show counts.
names = ['bob', 'susan', 'bob', 'dan', 'susan']
uniques = []
duplicates = []
for name in names:
    if name not in uniques:
        uniques.append(name)
    elif name in uniques:
        duplicates.append(name)
print('Unique list: ', uniques)
print('Duplicate list: ', duplicates)

# Since we need to find if the word exists in the object - lists are inefficient
# at this since we have to search through each element
# Now we will use sets to do the same problem.

unique_names = set(names)
print(unique_names)

# Now we just have uniques names through Data Structure Magic.
# But we don't have the counts OR the duplicates. So... if only we only track it with an accompanying counter.
# Note we cant do a set difference since we would convert the list of names to a set and thus wipe duplicates.

name_count = {} # declare empty dictionary
for name in names:
    if name not in name_count:
        name_count[name] = 1
    else:
        name_count[name] += 1
print('name_count', name_count.items())
print('name_count  1 ', list(name_count.items())[0])
final_names = [f'{key}({value})' for key, value in name_count.items()]
print('final names: ', ' '.join(final_names))

print('-----------Default Dictionary-----------------')

from collections import defaultdict
name_count = defaultdict(int) # declare empty dictionary
for name in names:
    name_count[name] += 1 # The default dict adds in the name and initializes the value to 0.
    # Then it adds a 1
print('name_count', name_count)
final_names = [f'{name}({count})' for name, count in name_count.items()]
print('final names: ', ' '.join(final_names))

print('-----------Counter for duplicate names-----------------')

from collections import Counter
name_count = Counter(names) #Counter is dictionary that stores the "count" of each key as it corresponding value.
print('name_count', name_count)
final_names = [f'{name}({count})' for name, count in name_count.items()]
print('final names: ', ' '.join(final_names))

print('-----------Counter for duplicate letters-----------------')

duplicate_leters = Counter('indiVISABility'.lower())
final_letters = [f'{letter}({count})' for letter, count in duplicate_leters.items()]
print('Finals Letters are: ', ' '.join(final_letters))