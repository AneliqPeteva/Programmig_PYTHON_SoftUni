
def team_lineup(*args):
    team = {}
    for data in args:
        name = data[0]
        country = data[1]
        if country not in team:
            team[country] = []
        team[country].append(name)

    team = sorted(team.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for current_country, players in team:
        result += f'{current_country}:\n'
        for current_player in players:
            result += f'  -{current_player}\n'

    return result







# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))
# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))
