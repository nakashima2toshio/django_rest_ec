from rest_framework import viewsets
from ec_app.models import Customer, CustomerProfile, Order, Product, Category, ProductCategory
from ec_app.serializers import CustomerSerializer, CustomerProfileSerializer, OrderSerializer, ProductSerializer, \
    CategorySerializer, ProductCategorySerializer

"""
to use ModelViewSet, you need to define queryset and serializer_class
"""


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


"""
Class based views for the API
"""
# from rest_framework import generics
# from ec_app.models import Customer, CustomerProfile, Order, Product, Category, ProductCategory
# from ec_app.serializers import CustomerSerializer, CustomerProfileSerializer, OrderSerializer, ProductSerializer, \
#     CategorySerializer, ProductCategorySerializer
#
#
# class CustomerList(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#
# class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#
# class CustomerProfileList(generics.ListCreateAPIView):
#     queryset = CustomerProfile.objects.all()
#     serializer_class = CustomerProfileSerializer
#
#
# class CustomerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomerProfile.objects.all()
#     serializer_class = CustomerProfileSerializer
#
#
# class OrderList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class ProductCategoryList(generics.ListCreateAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = ProductCategorySerializer
#
#
# class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ProductCategory.objects.all()
#     serializer_class = ProductCategorySerializer
