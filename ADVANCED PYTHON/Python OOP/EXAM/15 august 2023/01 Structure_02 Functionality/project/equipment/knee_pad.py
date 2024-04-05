from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(120, 15.0)

    def increase_price(self):
        self.price += self.price * 0.20
        return self.price