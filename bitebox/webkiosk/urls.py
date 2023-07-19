from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name ='webkiosk'

urlpatterns = [
    # http://localhost:8000/webkiosk/
    path('', views.index, name='index'),

    # http://localhost:8000/webkiosk/menu/
    path('menu/', views.listfood, name='food-list'),

    # http://localhost:8000/webkiosk/food/new/
    path('food/new/', views.createfood, name = 'food-create'),

    # http://localhost:8000/webkiosk/food/1/
    path('food/<int:pk>/', views.detailfood, name='food-detail'),

    # http://localhost:8000/webkiosk/food/1/edit/
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),

    # http://localhost:8000/webkiosk/food/1/delete/
    path('food/<int:pk>/delete/', views.deletefood, name = 'food-delete'),

    # everything past this point would be customer related
    # http://localhost:8000/webkiosk/customer/
    path('customer/', views.customerlist, name="customer-list"),

    # http://localhost:8000/webkiosk/customer/new
    path('customer/new', views.createcustomer, name="customer-create"),

    # http://localhost:8000/webkiosk/customer/1
    path('customer/<int:pk>/', views.detailcustomer, name='customer-detail'),  

    # http://localhost:8000/webkiosk/customer/1/edit
    path('customer/<int:pk>/edit/', views.editcustomer, name='customer-edit'),  

    # http://localhost:8000/webkiosk/customer/1/delete
    path('customer/<int:pk>/delete', views.deletecustomer, name="customer-delete"),

    # everything below this is going for the orders related
    # http://localhost:8000/webkiosk/order/
    path('order/', views.orderlist, name="order-list"),

    # http://localhost:8000/webkiosk/order/new
    path('order/new', views.createorder, name="order-create"),

    # http://localhost:8000/webkiosk/customer/1
    path('order/<int:pk>/', views.detailorder, name='order-detail'),  

    # http://localhost:8000/webkiosk/customer/1/edit
    path('order/<int:pk>/edit/', views.editorder, name='order-edit'),  

    # http://localhost:8000/webkiosk/customer/1/delete
    path('order/<int:pk>/delete', views.deleteorder, name="order-delete"),

    # http://localhost:8000/webkiosk/customer/1/order
    path('customer/<int:customer_id>/order', views.customer_order, name='customer-order-detail'),

    # http://localhost:8000/webkiosk/login/
    path('login/', views.login_view, name="login"), 

    #http:localhost:8000/webkiosk/logout/
    path('logout/', auth_views.LogoutView.as_view(next_page='webkiosk/login'), name='logout'),
  

] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)