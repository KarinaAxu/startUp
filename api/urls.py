from django.urls import path
<<<<<<< HEAD
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/introspect/', views.TokenIntrospectView.as_view(), name='token-introspect'),
    path('dishes/', views.DishList.as_view(), name='dish-list'),
    path('dish/<int:pk>/', views.DishDetail.as_view(), name='dish-detail'),
    # path('restaurants/', views.RestaurantList.as_view(), name='restaurant-list'),
    # path('restaurant/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant-detail'),
    # path('menu/<int:pk>/', views.MenuDetail.as_view(), name='menu-detail'),
    path('restaurants/', views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurant/<int:pk>/', views.RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),
    path('menus/', views.MenuListCreateView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.MenuRetrieveUpdateDestroyView.as_view(), name='menu-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('order_items/', views.OrderItemList.as_view(), name='order-item-list'),
    path('api/order_item/<int:pk>/', views.OrderItemDetail.as_view(), name='order-item-detail'),
]
=======
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dishes/', views.DishList.as_view(), name='dish_list_create'),
    path('dishes/<int:pk>/', views.DishDetail.as_view(), name='dish_detail'),

    path('couriers/', views.CourierList.as_view(), name='courier_list_create'),
    path('couriers/<int:pk>/', views.CourierDetail.as_view(), name='courier_detail'),

    path('customers/', views.CustomerList.as_view(), name='customers_list_create'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customers_detail'),

    path('restaurants/', views.RestaurantList.as_view(), name='restaurant_list_create'),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),

    path('menus/', views.MenuList.as_view(), name='menu_list_create'),
    path('menus/<int:pk>/', views.MenuDetail.as_view(), name='menu_detail'),

    path('orders/', views.OrderListCreate.as_view(), name='order_list_create'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),

    path('order_items/', views.OrderItemListCreate.as_view(), name='order_item_list_create'),
    path('order_items/<int:pk>/', views.OrderItemDetail.as_view(), name='order_item_detail'),

    path('payments/', views.PaymentListCreate.as_view(), name='payment_list_create'),
    path('payments/<int:pk>/', views.PaymentDetail.as_view(), name='payment_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147
