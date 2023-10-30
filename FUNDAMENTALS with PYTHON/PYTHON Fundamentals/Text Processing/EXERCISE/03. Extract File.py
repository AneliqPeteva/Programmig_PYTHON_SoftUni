# data = input().split("\\")
# point = data[-1].find(".")
# file_name = data[-1][:point]
# file_extension = data[-1][point + 1:]
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")

data = input().split("\\")
name, extensions = data[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extensions}")