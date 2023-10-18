class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)
    def get_by_letter(self, first_letter):
        filtered_catalog = []

        for product in self.products:
            if product[0] == first_letter:
                filtered_catalog.append(product)
        return filtered_catalog
    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"

        for product in sorted(self.products):
            result += "\n" + product
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
