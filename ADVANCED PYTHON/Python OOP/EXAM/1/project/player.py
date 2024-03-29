class Player:
    unique_name = []
    def __init__(self, name:str, age:int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        elif value in Player.unique_name:
            raise Exception(f"Name {value} is already used!")

        Player.unique_name.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value
        
    @property
    def stamina(self):
        return self.__stamina
    
    @stamina.setter
    def stamina(self, value):
        if 0 < value or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

