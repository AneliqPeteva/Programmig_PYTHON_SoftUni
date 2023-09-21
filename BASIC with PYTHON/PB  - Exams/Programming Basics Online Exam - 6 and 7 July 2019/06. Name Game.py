#User input
name = input()
winner = ""
max_total = 0
#logic
while True:
    if name == "Stop":
        break
    else:
        length_name = len(name)
        total_point = 0
        for i in range(length_name):

            number = int(input())
            if number == ord(name[i]):
                total_point += 10
            else:
                total_point += 2
    if max_total <= total_point:
        max_total = total_point
        winner = name
    name = input()
#print output
print(f"The winner is {winner} with {max_total} points!")
