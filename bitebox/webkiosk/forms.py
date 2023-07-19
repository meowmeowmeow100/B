from django.forms import ModelForm
from .models import Food
from .models import Customer
from .models import Order

class FoodForm(ModelForm):
    class Meta:
        model = Food 
        #fields from food model that want to import to here, but not necessary that all are here
        fields = ['name', 'description', 'price']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        #fields from customer model that want to import to here, but not necessary that all are here
        fields = ['firstname', 'lastname', 'address', 'city']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['paymentmode', 'quantity', 'food', 'customer']
