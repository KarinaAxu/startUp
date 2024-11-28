from rest_framework import serializers
<<<<<<< HEAD

from store.models import Dish, Restaurant, Menu, Order, OrderItem, Payment, Customer, Courier

=======
from store.models import Dish, Customer, Courier, Restaurant, Menu, Order, OrderItem, Payment
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
<<<<<<< HEAD
        exclude = ('created_at', 'updated_at')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ('created_at', 'updated_at')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        exclude = ('created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ('created_at', )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

=======
        fields = '__all__'

    def validate_price(self, value):
        if not (100 <= value <= 100000):
            raise serializers.ValidationError("Цена должна быть между 100 и 100000.")
        return value
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

<<<<<<< HEAD

=======
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147
class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
<<<<<<< HEAD
=======

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147
