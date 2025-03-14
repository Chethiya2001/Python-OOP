from item import Item

class Phone(Item):
    
    def  __init__(self,name:str, price: float, quantity=0, broken_phone=0):
        assert broken_phone >= 0 , f"Broken Phone {quantity} is not equel or greater than 0"
        
        super().__init__(
            name,price,quantity
        )
        self.broken_phone = broken_phone       
    def  __repr__(self):
        return f"{self.__class__.__name__}{self.name}','{self.quantity}','{self.price}"