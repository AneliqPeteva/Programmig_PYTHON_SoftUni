from typing import List


class SteamUser:
    def __init__(self, username: str, games: List[str]):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, cur_game: str, cur_hours: int):
        if cur_game in self.games:
            self.played_hours += cur_hours
            return f"{self.username} is playing {cur_game}"
        return f"{cur_game} is not in library"

    def buy_game(self, cur_game):
        if cur_game not in self.games:
            self.games.append(cur_game)
            return f"{self.username} bought {cur_game}"
        return f"{cur_game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"




user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
