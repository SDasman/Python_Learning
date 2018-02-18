test_word = 'door'
test_sentence = 'I went to the door and saw my brother and we had some fun times.'
translated_sentence = ''

englishtohindi = {
    'door': 'darwaza',
    'fun': 'maaza',
    'brother': 'bhaijaan',
    'red': 'laal',
    'food': 'khana'
}

key = test_word
for key in test_sentence.split():
    if key in englishtohindi:
        translated_sentence += englishtohindi[key] + ' '
    else:
        translated_sentence += key  + ' '

print(test_word)
print(test_sentence)
print(translated_sentence)
