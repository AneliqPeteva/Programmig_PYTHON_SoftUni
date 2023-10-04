def all_sum(all_number):
     even_total = 0
     odd_total = 0
     for num in all_number:
         num = int(num)
         if num % 2 == 0:
             even_total += num
         else:
             odd_total += num
     return f"Odd sum = {odd_total}, Even sum = {even_total}"

numbers = input()
print(all_sum(numbers))