from django import forms
<<<<<<< HEAD

from store.models import Dish

=======
from store.models import Dish, Customer, Courier, Restaurant, Menu, Order, OrderItem, Payment
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
<<<<<<< HEAD
        fields = ('name', 'description', 'price', 'is_available', )
        # exclude = ['description']


class UpdateDishForm(forms.Form):
    price = forms.IntegerField()
=======
        fields = '__all__'

class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['price']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147
