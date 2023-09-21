# Read user input

day_week = input()
ticket_price = 0
# Logic
if day_week == "Monday" or day_week == "Tuesday" or day_week == "Friday":
    ticket_price = 12
elif day_week == "Wednesday" or day_week == "Thursday":
    ticket_price = 14
elif day_week == "Saturday" or day_week == "Sunday":
    ticket_price = 16
# Print output
print(ticket_price)