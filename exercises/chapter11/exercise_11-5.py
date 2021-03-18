from exercises.chapter8 import exercise_8_5

def rotate_pairs(word_dict):
    rot_pairs = {}
    for word in word_dict:
        for i in range(1, 25):
            rot_word = exercise_8_5.rotate_word(word, i)
            if rot_word in word_dict:
                rot_pairs[(word, i)] = rot_word
    return rot_pairs


print(rotate_pairs({'b': None, 'a': None}))