# 9.3

def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True


with open('words.txt') as word_list:
    forbidden_letters = input('Enter the forbidden letters: ')
    for word in word_list:
        if avoids(word, forbidden_letters):
            print(word.strip() + ' doesn\'t have the forbidding letters in it')
