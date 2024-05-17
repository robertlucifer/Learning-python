import csv


# noinspection PyTypeChecker
class Item:
    discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validating the values provided
        assert price > 0, f"Price cannot be zero or negative"
        assert quantity >= 0, f"quantity cannot be zero or negative"

        # assigning the values
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # action which is used to all the instance to a list
        Item.all.append(self)
        # or you can do item.all.append(self.name)

    @property
    def price(self):
        return self.__price

    def price_after_discount(self):
        self.__price = self.__price * self.discount

    def increment_price_by_percent(self, percent):
        self.__price = self.__price + self.__price * percent

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 10:
            self.__name = value
        else:
            raise Exception("The name is too long")

    def total_amount(self):
        return self.__price * self.quantity

    def __repr__(self) -> str:  # this is used by developers
        return f"{self.__class__.__name__} name:{self.name}, price:{self.__price} and quantity:{self.quantity}"

    @classmethod
    def instantiate_from_csv(cls, x):
        with open(x, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item1 in items:
            Item(
                name=item1.get("name"),
                price=float(item1.get("price")),
                quantity=int(item1.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @staticmethod
    def sample():
        return "robert"

    @property
    def read_only_name(self):
        return "aaa"

    def __create_body(self) -> str:
        return f"Hello Buddy {self.name}"

    def send(self):
        self.__connect("")
        value = self.__create_body()
        return value

    def __connect(self, smtp):
        pass

# item.instantiate_from_csv("items.csv")
# print(item.all)
# print(item.is_integer(2.0))


# child of item class


#
# phone1 = Phone("JscPhonev10", 500, 5, 1)
# print(phone1.total_amount())
# item1 = Item("sample", 500, 5)
# print(Phone.all)
# print(Item.all)
