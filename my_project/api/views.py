from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from catalog.models import Brand, Car, Customer, Order, Review, CarAccessory, Favorite
from .serializers import BrandSerializer, CarSerializer, CustomerSerializer, OrderSerializer, ReviewSerializer, \
    CarAccessorySerializer, UserSerializer, LoginSerializer, FavoriteCarSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class UserLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = Customer.objects.filter(username=username).first()

        print(f"Validate: Username: {username}, Password: {password}, User: {user}")

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            login(request, user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': str(user.username),
            })
        return Response({'detail': 'Invalid credentials111'}, status=401)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'detail': 'refresh_token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_comparison(request, car_id):
    favorite = get_object_or_404(Favorite, user=request.user, car__id=car_id)
    favorite.is_selected_for_comparison = True
    favorite.save()

    return Response({'message': 'Машина добавлена в сравнение'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sorted_favorite_cars(request, sort_method='default'):
    favorite_cars = (
        Favorite.objects
        .filter(user=request.user)
        .prefetch_related('car')
    )

    if sort_method == 'price-asc':
        favorite_cars = favorite_cars.order_by('car__price')
    elif sort_method == 'price-desc':
        favorite_cars = favorite_cars.order_by('-car__price')
    elif sort_method == 'year-asc':
        favorite_cars = favorite_cars.order_by('car__year')
    elif sort_method == 'year-desc':
        favorite_cars = favorite_cars.order_by('-car__year')

    serialized_data = FavoriteCarSerializer(favorite_cars, many=True).data
    return Response(serialized_data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite = Favorite.objects.filter(user=request.user, car=car).first()

    if favorite:
        favorite.delete()
        return Response({'message': 'Машина удалена из избранного'})
    else:
        return Response({'message': 'Машина не найдена в избранном'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, car=car)

    if created:
        return Response({'message': 'Машина добавлена в избранное'})
    else:
        return Response({'message': 'Машина уже находится в избранном'})


# class ProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         user = request.user
#         serializer = CustomerSerializer(user)
#         return Response(serializer.data)

class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class SearchCarListView(generics.ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()

        brand_id = self.request.query_params.get('brand')
        price_from = self.request.query_params.get('price_from')
        price_to = self.request.query_params.get('price_to')
        year_from = self.request.query_params.get('year_from')
        year_to = self.request.query_params.get('year_to')
        mileage = self.request.query_params.get('mileage')

        # Фильтрация по параметрам поиска
        if brand_id:
            queryset = queryset.filter(brand__id=brand_id)
        if price_from:
            queryset = queryset.filter(price__gte=price_from)
        if price_to:
            queryset = queryset.filter(price__lte=price_to)
        if year_from:
            queryset = queryset.filter(year__gte=year_from)
        if year_to:
            queryset = queryset.filter(year__lte=year_to)
        if mileage:
            queryset = queryset.filter(mileage__lte=mileage)

        return queryset

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BrandUpdateView(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BrandDeleteView(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

# class CarListView(generics.ListCreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CustomerDeleteView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class OrderDeleteView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class ReviewDeleteView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarAccessoryListView(generics.ListCreateAPIView):
    queryset = CarAccessory.objects.all()
    serializer_class = CarAccessorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarAccessoryCreateView(generics.CreateAPIView):
    serializer_class = CarAccessorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarAccessoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarAccessory.objects.all()
    serializer_class = CarAccessorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarAccessoryUpdateView(generics.UpdateAPIView):
    queryset = CarAccessory.objects.all()
    serializer_class = CarAccessorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class CarAccessoryDeleteView(generics.UpdateAPIView):
    queryset = CarAccessory.objects.all()
    serializer_class = CarAccessorySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from .urls.py import Brand
# from .serializers import BrandSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import render, redirect
# from rest_framework_simplejwt.views import TokenObtainPairView
#
# def custom_login_view(request):
#     if request.method == 'POST':
#         # Обработка POST-запроса и выдача токена
#         token_view = TokenObtainPairView.as_view()
#         return token_view(request)
#
#     # Если это GET-запрос, отображаем страницу входа
#     return render(request, 'login.html')
#
#
# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer


# class BrandAPIList(generics.ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandAPIUpdate(generics.UpdateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

