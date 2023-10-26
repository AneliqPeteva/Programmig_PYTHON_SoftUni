results = {}
submission = {}

while True:
    command = input().split("-")
    if len(command) == 1:
        break
    elif len(command) == 2:
        del results[command[0]]
    elif len(command) == 3:
        username, current_language, current_point = command[0], command[1], int(command[2])
        if username not in results.keys():
            results[username] = 0
        if results[username] < current_point:
            results[username] = current_point

        if current_language not in submission.keys():
            submission[current_language] = 0
        submission[current_language] += 1

print("Results:")
for user_name, points in results.items():
    print(f"{user_name} | {points}")
print("Submissions:")
for language, submissions_count in submission.items():
    print(f"{language} - {submissions_count}")