class Magazine:
    def __init__(self, vol:float):
        self.vol = vol
        self.products = []


    def __storage_check(self):
        sum_products = sum([x.vol for x in self.products])
        return self.vol - sum_products

    def add(self , product):
        rest_vol = self.__storage_check()
        if rest_vol >= product.vol:
            self.products.append(product)
            return rest_vol - product.vol
        else:
            return -1


class Product:
    def __init__(self, name:str, vol:float):
        self.name = name
        self.vol = vol


mag = Magazine(10)
prod = Product("batonik", 2)
prod2 = Product("napój", 5)
print(mag.products)
mag.add(prod)
print(mag.products)
mag.add(prod2)
print(mag.products)