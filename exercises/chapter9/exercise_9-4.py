# 9.4

def uses_only(word, only_use_letters):
    charset = list(set(word.strip()))
    for char in charset:
        if char not in only_use_letters:
            return False
    return True


with open('words.txt') as word_list:
    only_use_letters = input('Enter the only wanted letters in a word: ')
    for word in word_list:
        if uses_only(word, only_use_letters):
            print(word.strip() + ' only uses characters from the letters: ' + only_use_letters)
