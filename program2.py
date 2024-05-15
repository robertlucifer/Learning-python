import csv
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
    
    @classmethod
    def instantiate_from_csv(cls,x):
        with open(x,'r')as f:
            reader=csv.DictReader(f)
            items=list(reader)
        
        for item1 in items:
            item(
                name=item1.get('name'),
                price=float(item1.get('price')),
                quantity=int(item1.get('quantity'))
            )
            

item.instantiate_from_csv("items.csv")
print(item.all)
