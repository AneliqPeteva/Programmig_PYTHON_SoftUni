# Read user input
n = int(input())
salary = int(input())

# Logic
for i in range(n):
    open_tab = input()
    if open_tab == "Facebook":
        salary -= 150
    elif open_tab == "Instagram":
        salary -= 100
    elif open_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break

# Print output
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)



