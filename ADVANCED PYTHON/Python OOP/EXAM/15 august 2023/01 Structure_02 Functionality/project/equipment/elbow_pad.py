from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(90, 25.0)

    def increase_price(self):
        self.price = self.price + self.price * 0.10
        return self.price