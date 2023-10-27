contest_judge = {}
individual_dict = {}
command = input().split(" -> ")

while command[0] != "no more time":
    username, contest, points = command[0], command[1], int(command[2])
    contest_judge[contest] = contest_judge.get(contest, {})
    contest_judge[contest][username] = contest_judge[contest].get(username, 0)
    contest_judge[contest][username] = max(points, contest_judge[contest][username])

    command = input().split(" -> ")

for contest in contest_judge.keys():
    print(f"{contest}: {len(contest_judge[contest])} participants")
    for position, (user, score) in enumerate(sorted(contest_judge[contest].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{position}. {user} <::> {score}")
        individual_dict[user] = individual_dict.get(user, 0) + score

print("Individual standings:")
for position, (user, score) in enumerate(sorted(individual_dict.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {user} -> {score}")
