# one challenge with program is with representing data
# for basic data, we can use primitive data types and collections

# we can create a property so that we can abstract the attribute away
class Customer:
    # define the attributes of the customer 
    def __init__(self, name, membership_type):
        # anytime we invoke the customer, we want this to run, so any code that we'll want to run when the customer is created will be executed here
        self.name = name
        self.membership_type = membership_type

    # i want too make some atrributes as properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name
# any time we need some custom functionality
    # if i want to print or convert an object or instance of this class into string 
    def __str__(self):
        return self.name + ' '+ self.membership_type
    
    __repr__ = __str__
    
    # whenever you want to compare some values of two objects we can use the __eq__ method 
    def __eq__(self, other):
        # business logic for the __eq__
        #  two instances c and d when we do c = d
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    
    def print_all_customers(customers):
        # this function is not specific to a user but generic 
        # so we'll apply it to the class itself to get the objects of the class
        for customer in customers:
            print(customer) 
    
c = Customer('kelvin', 'Gold')
d =Customer(name='mark', membership_type='bronze')
c.membership_type = 'bronze'
# so i don't need to print the individual attributes of this customer
customers = [Customer(name='mark', membership_type='bronze'),
             Customer(name='Aaron', membership_type= 'Gold')]
Customer.print_all_customers(customers=customers)
print(customers)

customer_are_equal = c == d
print(customer_are_equal)
