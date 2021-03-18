def has_duplicates(input):
    item_dict = {}
    for item in input:
        if item in item_dict:
            return True
        item_dict[item] = True
    return False
