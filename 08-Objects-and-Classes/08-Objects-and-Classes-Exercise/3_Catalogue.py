class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # return [product for product in self.products if product.startswith(first_letter)]
        products_by_letter = []
        for product in self.products:
            if product[0] == first_letter:
                products_by_letter.append(product)
        return products_by_letter

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return returning_string



###########



class Catalogue:

    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        catalogue_ = [product for product in self.products if product.startswith(first_letter)]
        return catalogue_

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result