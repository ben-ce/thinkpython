# 9.6

def is_abecedarian(word):
    char_list = list(word.strip())
    if all(char_list[i] <= char_list[i+1] for i in range(len(char_list)-1)):
        print(word.strip() + ' is a sorted list of characters')


with open('words.txt') as word_list:
    for word in word_list:
        is_abecedarian(word)
