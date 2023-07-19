from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    def get_customer_initials(self): #custom methods to get customer initials
        return self.firstname[0] + self.lastname[0]

    def __str__(self):
        return f'''CUSTOMER #{self.id}: 
        NAME: {self.firstname} {self.lastname} 
        ADDRESS: {self.address}
        CITY: {self.city}'''

class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_food_shortname(self):
        return self.name[0:3]

    def __str__(self):
        return f'''FOOD #{self.id}
        NAME: {self.name}
        DESCRIPTION: {self.description}
        PRICE: {self.price}'''

class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'),
        ('CD', 'Card'),
        ('DW', 'Digital Wallet'),
    ]
    #manytomany relationship, make another class
    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    quantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'''ORDER #{self.id}
        FOOD NAME: {self.food.name}
        FOOD QUANTITY: {self.quantity}
        PAYMENT MODE: {self.paymentmode}
        ORDER DATE AND TIME: {self.orderdatetime}'''