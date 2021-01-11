# 9.5

def uses_all(word, all_letters):
    charset = list(set(word.strip()))
    for letter in all_letters:
        if letter not in charset:
            return False
    return True


with open('words.txt') as word_list:
    required_letters = input('Enter the required letters: ')
    for word in word_list:
        if uses_all(word, required_letters):
            print(word.strip() + ' uses all letters at least once from ' + required_letters)
