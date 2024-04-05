from typing import List


class Controller:
    VALID_TYPES = [
        "Food",
        "Dring",
    ]
    def __init__(self):
        self.players: List = []
        self.supplies: List = []

    def add_player(self, *args):
        added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)
        return f"Successfully added: {', '.join(added)}"

    def add_supplies(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name:str, sustenance_type:str):
        if sustenance_type not in self.VALID_TYPES:
            return

        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):








