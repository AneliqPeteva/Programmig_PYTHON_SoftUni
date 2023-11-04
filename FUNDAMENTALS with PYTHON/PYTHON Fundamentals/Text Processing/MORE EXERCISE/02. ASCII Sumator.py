start_symbol = input()
last_symbol = input()
text = input()

total_sum = [ord(symbol) for symbol in text if ord(start_symbol) < ord(symbol) < ord(last_symbol)]
print(sum(total_sum))


# def total_sum(start, end, string):
#     total_sum = 0
#     for symbol in string:
#         if ord(start) < ord(symbol) < ord(end):
#             total_sum += ord(symbol)
#     return total_sum
#
# start_symbol = input()
# last_symbol = input()
# text = input()
#
# print(total_sum(start_symbol, last_symbol, text))


# start_symbol = input()
# last_symbol = input()
# text = input()
#
# total_sum = 0
# for current_symbol in text:
#     if ord(start_symbol) < ord(current_symbol) < ord(last_symbol):
#         total_sum += ord(current_symbol)
# print(total_sum)