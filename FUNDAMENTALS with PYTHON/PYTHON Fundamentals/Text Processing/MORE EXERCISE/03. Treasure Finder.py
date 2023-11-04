# secret_key = [int(x) for x in input().split()]
# secret_msg = input()
#
# how_long = len(secret_key)
# while secret_msg != "find":
#     secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
#     item = secret_text.split("&")[-2]
#     location = secret_text.split("<")[-1][:-1]
#     print(f"Found {item} at {location}")
#     secret_msg = input()

secret_key = [int(x) for x in input().split()]
secret_message = input()
how_long = len(secret_key)

while secret_message != "find":
    secret_text = []
    for current_element in range(len(secret_message)):
        new_current_symbol = ord(secret_message[current_element]) - secret_key[current_element % how_long]
        new_current_symbol = chr(new_current_symbol)
        secret_text.append(new_current_symbol)
    secret_text = "".join(secret_text)
    item = secret_text.split("&")[1]
    location = secret_text.split("<")[-1][0:-1]
    print(f"Found {item} at {location}")
    secret_message = input()