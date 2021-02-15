def nested_sum(test_list):
    list_sum = 0
    for item in test_list:
        if isinstance(item, list):
            list_sum += nested_sum(item)
        else:
            list_sum += item
    return list_sum


test_list = [1, 2, 3, [4, 5, [1, 2]]]
print(nested_sum(test_list))
