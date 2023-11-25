# def add_stop(ind, text):
#     if 0 <= ind < len(text_travel) and 0 <= ind < len(text_travel):
#         result = text_travel[:ind] + text + text_travel[ind:]
#         return result
#     return text_travel
#
# def remove_stop(start_ind, end_ind):
#     if 0 <= start_ind < len(text_travel) and 0 <= end_ind < len(text_travel):
#         result = text_travel[:start_ind] + text_travel[end_ind + 1:]
#         return result
#     return text_travel
#
# def switch(old, new):
#     if old in text_travel:
#         result = text_travel.replace(old, new)
#         return result
#     return text_travel
#
# text_travel = input()
#
# command = input().split(":")
# while command[0] != "Travel":
#     if command[0] == "Add Stop":
#         index = int(command[1])
#         string = command[2]
#         text_travel = add_stop(index, string)
#         print(text_travel)
#     elif command[0] == "Remove Stop":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         text_travel = remove_stop(start_index, end_index)
#         print(text_travel)
#     elif command[0] == "Switch":
#         old_string = command[1]
#         new_string = command[2]
#         text_travel = switch(old_string, new_string)
#         print(text_travel)
#
#     command = input().split(":")
#
# print(f"Ready for world tour! Planned stops: {text_travel}")


API
TOOLS
FAQ
paste
Search...

LOGIN
SIGN
UP
Advertisement

SHARE
TWEET
Guest
User
exam_preparation
A
GUEST
NOV
24
TH, 2023
119
0
NEVER
ADD
COMMENT
Not
a
member
of
Pastebin
yet? Sign
Up, it
unlocks
many
cool
features!
4.20
KB | None |

# 1
stops = input()
command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, some_string = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + some_string + stops[index:]
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")