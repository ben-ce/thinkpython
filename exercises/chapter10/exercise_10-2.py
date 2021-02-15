def cumsum(test_list):
    list_sum = []
    i = 0
    for item in test_list:
        list_sum.append(sum(test_list[:i+1]))
        i += 1
    return list_sum


test_list = [1, 2, 3]
print(cumsum(test_list))
