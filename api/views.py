from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from api.filters import RestaurantFilter, MenuFilter
from api.serializers import DishSerializer, RestaurantSerializer, MenuSerializer, OrderSerializer, OrderItemSerializer
from store.models import Dish, Restaurant, Menu, Order, OrderItem


class TokenIntrospectView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        token = request.data.get("token")

        if not token:
            return Response({"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            access_token = AccessToken(token)
            return Response(data={
                "active": True,
                "token_type": access_token["token_type"],
                "exp": access_token["exp"],
                "user_id": access_token["user_id"],
            }, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"active": False}, status=status.HTTP_400_BAD_REQUEST)


class DishList(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )


class DishDetail(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny, )


class RestaurantListCreateView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RestaurantFilter
    ordering_fields = ['name', 'created_at']


class RestaurantRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# class RestaurantList(generics.ListAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
#     authentication_classes = ()
#     permission_classes = (permissions.AllowAny, )
#
# class RestaurantDetail(generics.RetrieveAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
#     authentication_classes = ()
#     permission_classes = (permissions.AllowAny, )
#
# class MenuDetail(generics.RetrieveAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     authentication_classes = ()
#     permission_classes = (permissions.AllowAny, )

class MenuListCreateView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MenuFilter
    ordering_fields = ['name', 'created_at']

class MenuRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

from rest_framework import generics
from store.models import Dish, Customer, Courier, Restaurant, Menu, Order, OrderItem, Payment
from api.serializers import DishSerializer, CourierSerializer, CustomerSerializer, RestaurantSerializer, MenuSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer

class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Dish.objects.filter(is_available=True)
        return super(DishList, self).get(request, *args, **kwargs)

class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CourierList(generics.ListAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class CourierDetail(generics.RetrieveAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )


class OrderItemList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
