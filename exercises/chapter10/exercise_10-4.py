def chop(test_list):
    del test_list[0]
    del test_list[-1]


test_list = [1, 2, 3, 4]
chop(test_list)
print(test_list)
