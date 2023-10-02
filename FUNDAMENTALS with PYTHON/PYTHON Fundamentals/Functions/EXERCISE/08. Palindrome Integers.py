def palindrome_integers(some_number):
    if some_number == some_number[::-1]:
        return True
    return False

list_number = input().split(", ")
for current_num in list_number:
    print(palindrome_integers(current_num))
