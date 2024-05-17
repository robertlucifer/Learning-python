from item import Item
from phone import Phone

# Item.instantiate_from_csv("items.csv")
item1 = Item("Asus Tuf", 2000, 5)
print(item1.name)
item1.name = "Dell"
print(item1.price)
item1.increment_price_by_percent(0.2)
print(int(item1.price))

item1.price_after_discount()
print(item1.price)
print(item1.send())
