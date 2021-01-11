
def is_palindrome(word):
    return word == word[::-1]


i = 0
while i < 1000000:
    j = str(i).zfill(6)
    if is_palindrome(j[2:]):
        original_number = j
        j = str(i+1).zfill(6)
        if is_palindrome(j[1:]):
            j = str(i+2).zfill(6)
            if is_palindrome(j[1:len(j)-1]):
                j = str(i+3).zfill(6)
                if is_palindrome(j):
                    print('This is the number: ' + original_number)
    i += 1
