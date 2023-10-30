# usernames = input().split(", ")
#
# for username in usernames:
#     if 3 <= len(username) <= 16:
#         if username.isalnum() or "-" in username or "_" in username:
#             if " " not in username:
#                 print(username)

def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username):
    if username.isalnum() or "-" in username or "_" in username:
        return True
    return False

def no_redundant_symbols(username):
    if " " not in username:
        return True
    return False
def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False

usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)