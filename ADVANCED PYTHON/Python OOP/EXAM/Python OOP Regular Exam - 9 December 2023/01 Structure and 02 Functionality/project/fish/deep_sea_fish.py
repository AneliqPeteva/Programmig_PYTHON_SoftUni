from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)

    def fish_details(self):
        return f"{type(self).__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"

