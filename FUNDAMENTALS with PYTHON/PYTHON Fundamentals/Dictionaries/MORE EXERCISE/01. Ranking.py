contests = {}
submissions = {}
command_contents = input().split(":")
while command_contents[0] != "end of contests":
    contest, password_for_contest = command_contents[0], command_contents[1]
    contests[contest] = password_for_contest
    command_contents = input().split(":")

command_submissions = input()
while command_submissions != "end of submissions":
    contest_name, password, username, points = command_submissions.split("=>")
    if contest_name not in contests.keys() or password != contests[contest_name]:
        command_submissions = input()
        continue
    submissions[username] = submissions.get(username, {})
    submissions[username][contest_name] = submissions[username].get(contest_name, 0)
    submissions[username][contest_name] = max(int(points), submissions[username][contest_name])
    command_submissions = input()

max_user, max_total_score = max(submissions.items(), key=lambda user_scores: sum(user_scores[1].values()))

print(f'Best candidate is {max_user} with total {sum(max_total_score.values())} points.\nRanking:')

for name in sorted(submissions):
    print(name)
    for current_contest, current_point in sorted(submissions[name].items(), key=lambda  item: -item[1]):
        print(f"#  {current_contest} -> {current_point}")
