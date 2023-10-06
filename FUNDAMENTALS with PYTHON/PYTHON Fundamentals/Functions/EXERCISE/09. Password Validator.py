# def password_validation(password):
#     errors = []
#     if not 6 <= len(password) <= 10:
#         errors.append("Password must be between 6 and 10 characters")
#     if not password.isalnum():
#         errors.append("Password must consist only of letters and digits")
#     if sum(1 for x in password if x.isdigit()) < 2:
#         errors.append("Password must have at least 2 digits")
#     return errors
#
#
# current_password = input()
# errors = password_validation(current_password)
# if errors:
#     [print(show) for show in errors]
# else:
#     print("Password is valid")


def password_validator(some_password: str) -> list:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
errors_in_password = password_validator(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))