class item:
    discount=0.8 #This is a class attribute where it is shared by all the instance (means all the the way you use this class like a datatype) this is constant and you can use it anywhere in this class it can be also updated outside the class by using the class name

    #this is a magic function which excuted when the specific class is created and it is mainly used to define the values in it
    def __init__(self, name: str , price:float, quantity=0):
        # validation
        assert price >=0, f"price {price} must be greater than 0"
        assert quantity >=0, f"quantity {quantity} must be greater than 0"

        #object
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_price(self):
        return self.price*self.quantity
    def applied_discount(self):
         self.price = self.price*self.discount
    

item1=item("phone", 2000, 3)
item1.applied_discount()
print(item1.price)
item2=item("laptop",2000,3)
item2.discount=0.5
item2.applied_discount()
print(item2.price)



# item1=item("phone", 2000, 3)
# # item1.applied_discount()
# # print(item1.price)

# item2=item("laptop",2000,3)
# item2.discount=0.5
# item2.applied_discount()
# print(item2.price)

# item.discount=0.9
# item1.applied_discount()
# print(item1.price)
# print(item2.price)
# # item1=item("phone", 2000, 3)

# # item2=item("laptop",200,3)
# # print(item1.calculate_total_price())
# # print(item.name)
# # item.name="Hello World"
# # print(item.__dict__)
# # print(item1.__dict__)#__dict__ is a magic function which is used to show the values of the object  and in instance level you about be able to see the class attribute because it is shared by all the instance and it is not shown in the instance level
# # print()