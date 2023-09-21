

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    curr_money = 0
    while curr_money < budget:
        all_money = float(input())
        curr_money += all_money
    print(f"Going to {destination}!")