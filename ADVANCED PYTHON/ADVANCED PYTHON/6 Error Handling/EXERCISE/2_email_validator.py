from re import findall

class MoreThanOneAtSymbol(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class NameTooLongError(Exception):
    pass


class InvalidDomainError(Exception):
    pass

class InvalidNameError(Exception):
    pass





VALID_DOMAINS = ("com", "bg", "net", "Org")
MIN_NAME_SYMBOLS_COUNT = 4
MAX_NAME_SYMBOLS_COUNT = 20

pattern_name = r'\w+'

email = input("Please input your email: ")

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only @ symbol!")

    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")

    elif len(email.split("@")[0]) >= MAX_NAME_SYMBOLS_COUNT:
        raise NameTooLongError("Name must be less than 20 characters!")

    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")

    elif findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscore")

    print("Email is valid")

    email = input("Please input your email: ")

