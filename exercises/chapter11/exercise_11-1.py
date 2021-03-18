def store_as_dict(words):
    word_dict = {}
    for word in words:
        word_dict[word.strip()] = True
    return word_dict


def string_in_dict(string, dict):
    if string in dict:
        return True
    return False
