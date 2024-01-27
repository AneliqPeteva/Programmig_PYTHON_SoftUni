# def sum_positive(positive_num):
#     return sum(positive_num)
# def sum_negative(negative_num):
#     return sum(negative_num)
#
#
#
# numbers = [int(x) for x in input().split()]
# positive = []
# negative = []
#
# for num in numbers:
#     if num < 0:
#         negative.append(num)
#     else:
#         positive.append(num)
#
# print(sum_negative(negative))
# print(sum_positive(positive))
#
# if abs(sum_positive(positive)) > abs(sum_negative(negative)):
#     print("The positives are stronger than the negatives")
# else:
#     print("The negatives are stronger than the positives")

def print_numbers(positive, negative):
    print(negative)
    print(positive)
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")



numbers = [int(x) for x in input().split()]
positive = sum(x for x in numbers if x > 0)
negative = sum(x for x in numbers if x < 0)

print_numbers(positive, negative)