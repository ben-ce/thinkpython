def in_bisect(list, target):
    if len(list) == 0:
        return False
    selected_word = list[len(list) // 2]
    if target == selected_word:
        return True
    if target < list[len(list) // 2]:
        return in_bisect(list[:len(list) // 2], target)
    else:
        return in_bisect(list[len(list) // 2 + 1:], target)


list = []
with open('words.txt') as word_file:
    for line in word_file:
        list.append(line.strip())

in_bisect(sorted(list), 'almafa')
