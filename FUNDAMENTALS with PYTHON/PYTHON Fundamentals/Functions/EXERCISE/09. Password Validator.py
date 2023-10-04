def password_validation(password):
    errors = []
    if not 6 <= len(password) <= 10:
        errors.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")
    if sum(1 for x in password if x.isdigit()) < 2:
        errors.append("Password must have at least 2 digits")
    return errors


current_password = input()
errors = password_validation(current_password)
if errors:
    [print(show) for show in errors]
else:
    print("Password is valid")