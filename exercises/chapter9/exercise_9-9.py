def check_ages(age_gap=None):
    i = 0
    diff_count = {}
    ages = []
    while i < 100:
        age_orig = str(i).zfill(2)
        age_reverse = age_orig[::-1]
        if age_orig != age_reverse and age_orig > age_reverse:
            j = int(age_reverse)
            diff = i - j
            if age_gap:
                if diff == age_gap:
                    ages.append(age_reverse)
            else:
                if diff not in diff_count:
                    diff_count[diff] = 1
                else:
                    diff_count[diff] += 1
        i += 1
    return diff_count, ages


diff_count, _ = check_ages()
for x in diff_count:
    if diff_count[x] >= 8:
        print('Possible age gap: {0}'.format(x))
        _, ages = check_ages(x)
        print('Based on the age gap the current age is: {0}'.format(ages[5]))
