def has_duplicates(test_list):
    test_list.sort()
    if any(test_list[i] == test_list[i+1] for i in range(0, len(test_list)-1)):
        return True
    return False
