import pdb
pdb.set_trace()
class item:
    discount=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity:int):
        #validating the values provided
        assert price >0,f"Price cannot be zero or negative"
        assert quantity>0,f"quantity cannot be zero or negative"

        #assigning the values
        self.name=name
        self.price=price
        self.quantity=quantity

        #action which is used to all the instance to a list
        item.all.append(self)
        #or you can do item.all.append(self.name)
    def total_amount(self):
        return self.price*self.quantity
    def price_after_discount(self):
        self.price=self.price*self.discount
    def __repr__(self)->str:#this is used by developers
        return f"item{self.name} and {self.price} and {self.quantity}"

        return f"Item('{self.name}',{self.price}, {self.discount})"
item1=item("phone",100,1)
item2=item("Laptop",1000,3)
item3=item("Cable",10,5)
item4=item("Mouse",50,5)
item5=item("Keyboard",75,5)

print(item.all)
