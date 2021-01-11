def double_consec(word):
    if len(word) < 5:
        return False
    consec_count = 0
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            consec_count += 1
            if consec_count == 3:
                return True
            i += 2
        else:
            consec_count = 0
            i += 1
    return False


with open('words.txt') as word_list:
    for word in word_list:
        if double_consec(word.strip()):
            print(word.strip() + ' is a triple double word')
