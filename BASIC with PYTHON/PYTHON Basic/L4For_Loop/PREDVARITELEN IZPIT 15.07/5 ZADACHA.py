current_status = 5364
top_mountain = 8848
counter_day_climbing = 1

command = input()
while command != "END":

    if command == "Yes":
        counter_day_climbing += 1

    elif command == "No":
        counter_day_climbing = counter_day_climbing

    else:
        current_status += int(command)
        if current_status >= top_mountain:
            print(f"Goal reached for {counter_day_climbing} days!")
            break
    if counter_day_climbing > 5:
        print("Failed!")
        print(f"{current_status}")
        break

    command = input()

else:
    print("Failed!")
    print(f"{current_status}")