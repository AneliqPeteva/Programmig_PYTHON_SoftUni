# Read user input
hours = int(input())
day = input()
# Logic
if day in ("Monday Tuesday Wednesday Thursday Friday Saturday"):
    if 10 <= hours <= 18:
        print("open")
    else:
        print("closed")
elif day == "Sunday":
    print("closed")
# Print output
