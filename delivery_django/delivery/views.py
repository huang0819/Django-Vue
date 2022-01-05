# Create your views here.
from delivery.models import Customer, Deliveryman, Food, Restaurant, Orderform
from delivery.serializers import CustomerSerializer, DeliverymanSerializer, FoodSerializer, RestaurantSerializer, OrderformSerializer

from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DeliverymanViewSet(viewsets.ModelViewSet):
    queryset = Deliveryman.objects.all()
    serializer_class = DeliverymanSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        rNo = self.request.query_params.get('rno')

        if rNo:
            queryset = queryset.filter(rno__exact=rNo)

        return queryset


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OrderformViewSet(viewsets.ModelViewSet):
    queryset = Orderform.objects.all()
    serializer_class = OrderformSerializer
