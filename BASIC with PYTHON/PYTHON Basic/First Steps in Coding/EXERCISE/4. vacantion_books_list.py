num_sheets_books = int(input())
sheet_hours = int(input())
num_days = int(input())

all_times_books = num_sheets_books//sheet_hours
hours_1day = all_times_books // num_days
print(hours_1day)