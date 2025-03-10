import csv
class Item:
    pay_rate =0.8 #pay rate after 20% discount
    all = []
    def  __init__(self,name:str, price: float, quantity=0):
      
        #validation for arguments
        assert price >= 0, f"Price {price} is not equel or greater than 0"
        assert quantity >= 0 , f"Quantity {quantity} is not equel or greater than 0"
        
        #Assing self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    def clacullateTotal(self):
        return self.price * self.quantity
    def discountRate(self):
       self.price = self.price * self.pay_rate
       
    @classmethod
    def intioansiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)#dictonary
            items = list(reader)#list
        for item in items:
            print(item)
    @staticmethod
    def is_intiger(num):
        # ex- 5.0 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else :
            return False
        
    def  __repr__(self):
        return f"{self.__class__.__name__}{self.name}','{self.quantity}','{self.price}"
    