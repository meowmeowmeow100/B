from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.forms import inlineformset_factory

from .models import Food, Customer, Order
from .forms import FoodForm, CustomerForm, OrderForm

def index(request):
    return render(request,'webkiosk/welcome.html')

def listfood(request):
    fl = Food.objects.all() 
    context = {'foodlist': fl}
    return render(request, 'webkiosk/food_list.html', context)

def createfood(request):
    if request.method == 'GET':
        f = FoodForm()
    elif request.method == 'POST':
        f = FoodForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('webkiosk:food-list')
        
    context = {'form': f, 'formheading': 'Add Food'}
    return render(request, 'webkiosk/food_form.html', context)

def detailfood(request, pk):
    f = Food.objects.get(id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated.')
    context = {'form': form, 'formheading': 'Update Food'}
    return render(request, 'webkiosk/food_form.html', context)

def deletefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food': f}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        f.delete()
        return redirect('webkiosk:food-list')

def customerlist(request):
    cl = Customer.objects.all() 
    context = {'customerlist': cl}
    return render(request, 'webkiosk/customer_list.html', context)

def createcustomer(request):
    if request.method == 'GET':
        c = CustomerForm()
    elif request.method == 'POST':
        c = CustomerForm(request.POST)
        if c.is_valid():
            c.save()
            return redirect('webkiosk:customer-list')
        
    context = {'form': c, 'formheading': 'Add Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def editcustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer)
    elif request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record successfully updated.')
    context = {'form': form, 'formheading': 'Update Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    c = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = {'customer': c}
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')

def orderlist(request):
    ol = Order.objects.all() 
    context = {'orderlist': ol}
    return render(request, 'webkiosk/order_list.html', context)

def createorder(request):
    if request.method == 'GET': #determines if request is GET or POST
        o = OrderForm()
    elif request.method == 'POST': #if submit button is submitted
        o = OrderForm(request.POST)
        if o.is_valid():
            o.save()
            return redirect('webkiosk:order-list') #internal redirect, can also be /webkiosk/menu
    context = {'form': o, 'formheading': 'Add Order'}
    return render(request, 'webkiosk/order_form.html', context)

def detailorder(request, pk):
    o = Order.objects.get(id=pk) 
    context = {'orderitem': o}
    return render(request, 'webkiosk/order_detail.html', context)

def editorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'GET':
        form = OrderForm(instance=order)
    elif request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order record successfully updated.')
    context = {'form': form, 'formheading': 'Update Order'}
    return render(request, 'webkiosk/order_form.html', context)

def deleteorder(request, pk):
    o = Order.objects.get(id=pk)
    if request.method == 'GET':
        context = {'order': o}
        return render(request, 'webkiosk/order_delete.html', context)
    elif request.method == 'POST':
        o.delete()
        return redirect('webkiosk:order-list')

#login shit

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webkiosk:food-list')
        else:
            return render(request, 'webkiosk/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'webkiosk/login.html')

def customer_order(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {"customer": customer, "orders": orders}
    return render (request, "webkiosk/customer_order.html", context)