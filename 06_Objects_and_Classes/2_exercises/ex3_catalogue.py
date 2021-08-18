class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        self.new_products = [x for x in self.products if x[0] == first_letter]
        return self.new_products

    def __repr__(self):
        self.products.sort()
        return f"Items in the {self.name} catalogue:\n" + "\n".join(self.products)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


