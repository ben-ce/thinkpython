def is_sorted(test_list):
    if all(test_list[i] <= test_list[i+1] for i in range(len(test_list)-1)):
        return True
    return False


def alt_is_sorted(test_list):
    return test_list == sorted(test_list)
