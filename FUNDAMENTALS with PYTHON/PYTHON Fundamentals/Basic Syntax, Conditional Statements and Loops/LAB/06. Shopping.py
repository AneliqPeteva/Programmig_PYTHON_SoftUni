budget = int(input())
command = input()
total_sum = 0

while command != "End":
    price = int(command)
    total_sum += price

    if total_sum > budget:
        print("You went in overdraft!")
        break
    command = input()

else:
    print("You bought everything needed.")


