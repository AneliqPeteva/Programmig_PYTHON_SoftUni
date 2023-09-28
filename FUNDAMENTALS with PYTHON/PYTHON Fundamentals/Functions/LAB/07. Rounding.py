input_number = list(map(float, input().split()))

def round_numbers(numbers):
    result = [round(num) for num in numbers]
    return result
print(round_numbers(input_number))