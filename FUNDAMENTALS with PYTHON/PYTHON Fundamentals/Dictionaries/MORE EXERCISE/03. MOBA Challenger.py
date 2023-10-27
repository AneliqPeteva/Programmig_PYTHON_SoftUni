pool = {}

command = input()
while command != 'Season end':
    if "->" in command:
        name, skill, points = command.split(" -> ")
        points = int(points)
        if name not in pool:
            pool[name] = {skill: points}
        elif name in pool and skill not in pool[name]:
            pool[name][skill] = points
        elif name in pool and skill in pool[name]:
            if pool[name][skill] < points:
                pool[name][skill] = points

    else:
        player_one, player_two = command.split(" vs ")
        if player_one in pool and player_two in pool:
            for position, points in pool[player_one].items():
                if position in pool[player_two].keys():
                    if points < pool[player_two][position]:
                        del pool[player_one]
                    elif pool[player_two][position] < pool[player_one][position]:
                        del pool[player_two]
                    break


    command = input()


total_points = {}
for name in pool.keys():
    for value in pool[name].values():
        if name not in total_points:
            total_points[name] = 0
        total_points[name] += value
total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))


for name in pool.keys():
    for k, v in pool[name].items():
        pool[name] = dict(sorted(pool[name].items(), key=lambda x: (-x[1], x[0])))

for name, totalpoints in total_points.items():
    print(f"{name}: {totalpoints} skill")
    for k, v in pool[name].items():
        print(f"- {k} <::> {v}")