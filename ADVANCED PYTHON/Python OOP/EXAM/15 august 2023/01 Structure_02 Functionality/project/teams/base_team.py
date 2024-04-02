from abc import ABC, abstractmethod
from math import floor
from typing import List


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value
        
    @property
    def advantage(self):
        return self.__advantage
    
    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass


    def get_statistics(self):
        total_price_of_team_equipment = sum(p.price for p in self.equipment)
        avg_team_protection = floor(sum(e.protection for e in self.equipment) / len(self.equipment)) if self.equipment else 0
        return (f"Name: {self.name}\n"
                f"Country: {self.country}"
                f"\nAdvantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n"
                f"Average Protection: {avg_team_protection}")

