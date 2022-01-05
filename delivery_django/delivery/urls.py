from django.urls import path, include


from rest_framework.routers import DefaultRouter

from delivery import views

customers_router = DefaultRouter()
customers_router.register(r'customers', views.CustomerViewSet)

deliverymen_router = DefaultRouter()
deliverymen_router.register(r'deliverymen', views.DeliverymanViewSet)

food_router = DefaultRouter()
food_router.register(r'foods', views.FoodViewSet)

restaurant_router = DefaultRouter()
restaurant_router.register(r'restaurants', views.RestaurantViewSet)

orderforms_router = DefaultRouter()
orderforms_router.register(r'orderforms', views.OrderformViewSet)


urlpatterns = [
    path('', include(customers_router.urls)),
    path('', include(deliverymen_router.urls)),
    path('', include(food_router.urls)),
    path('', include(restaurant_router.urls)),
    path('', include(orderforms_router.urls)),
]
