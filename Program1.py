class item:
    #this is a magic function which excuted when the specific class is created and it is mainly used to define the values in it
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_price(self):
        return self.price*self.quantity
        


item1=item("phone", 100, 5)

item2=item("laptop",1000,3)
print(item1.calculate_total_price())
print(item2.calculate_total_price())


