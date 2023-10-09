
def palindrome(word):
    if word == word[::-1]:
        return word


string = input().split(" ")
searching_palindrome = input()

palindorme_list = [word for word in string if palindrome(word)]
palindrome_counter = palindorme_list.count(searching_palindrome)
print(palindorme_list)
print(f'Found palindrome {palindrome_counter} times')
