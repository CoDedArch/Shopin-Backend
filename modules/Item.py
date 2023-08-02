# creation of a class 
# creation of the object
# we have class attributes and instance attributes 
# for class attributes they can be accessed at the instance level
import csv
class Item:
    # define
    pay_rate = 0.8
    all = []
    def __init__(self, name, price, quantity=0) -> None:
        # Run Validation to the received arguments
        assert price >= 0, f"price is not greater than or equal to 0"
        assert quantity >0, f"quantity is not greater than or equal to 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # action to execute
        Item.all.append(self)
        # we can always make assertions inside our classes

    def __repr__(self) -> str:
        return self.name

    def calculate_total_price(self, price, quantity):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    # this will be accessed from the class only
    @classmethod
    def instantiate_from_csv(cls):
        # using a context manager
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item (name= item['name'], price = int(item['price']), quantity= int(item['quantity']))
            

Item.instantiate_from_csv()
print(Item.all)

class Phone(Item):
    def __init__(self, name:str, price:float, quantity:int, broken_phones):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, "phone is broken"
        self.broken_phones = broken_phones