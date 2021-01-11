# 9.2

def has_no_e(word):
    if 'e' not in word:
        return True


no_e_count = 0
all_word_count = 0
with open('words.txt') as word_list:
    for word in word_list:
        if has_no_e(word):
            no_e_count += 1
            print(word)
        all_word_count += 1

print(str(no_e_count/all_word_count*100) + '% of the words in the list had no \'e\' in it')
