from rest_framework import serializers
from delivery.models import Customer, Deliveryman, Food, Restaurant, Orderform


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DeliverymanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveryman
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class OrderformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderform
        fields = '__all__'
