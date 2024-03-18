# from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from .views import CarListView, CarDetailView, UserRegistrationView, UserLoginView, BrandListView
#
# urlpatterns = [
#     path('users/register/', UserRegistrationView.as_view(), name='user-register'),
#     path('users/login/', UserLoginView.as_view(), name='user-login'),
#     path('cars/', CarListView.as_view(), name='car-list'),
#     path('brand/', BrandListView.as_view(), name='brand-list'),
#     path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
#     path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
#     path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
#     # Добавьте другие эндпоинты при необходимости
# ]



from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import (
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    UserRegistrationView, UserLoginView, LogoutView,
    BrandListView, BrandDetailView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
    CarAccessoryListView, CarAccessoryDetailView, CarAccessoryCreateView, CarAccessoryUpdateView,
    CarAccessoryDeleteView, add_to_favorites, remove_from_favorites, \
    get_sorted_favorite_cars, add_to_comparison, SearchCarListView
)

urlpatterns = [
    path('users/register/', UserRegistrationView.as_view(), name='user-register'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),

    path('user/profile/', CustomerDetailView.as_view(), name='profile-list'),
    path('user/profile/<int:pk>/', CustomerDetailView.as_view(), name='profile-detail'),

    path('add_to_favorites/<int:car_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:car_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('get_sorted_favorite_cars/<str:sort_method>/', get_sorted_favorite_cars, name='get_sorted_favorite_cars'),
    path('add_to_comparison/<int:car_id>/', add_to_comparison, name='add_to_comparison'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('cars/', SearchCarListView.as_view(), name='car-list'),


    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),  # Создание автомобиля
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),  # Редактирование автомобиля
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),  # Удаление автомобиля

    path('brand/', BrandListView.as_view(), name='brand-list'),
    path('brand/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brand/create/', BrandCreateView.as_view(), name='brand-create'),  # Создание бренда
    path('brand/<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),  # Редактирование бренда
    path('brand/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),  # Удаление бренда

    # path('customers/', CustomerListView.as_view(), name='customer-list'),
    # path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    # path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),  # Создание клиента
    # path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),  # Редактирование клиента
    # path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),  # Удаление клиента

    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review-create'),  # Создание отзыва
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),  # Редактирование отзыва
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),  # Удаление отзыва

    path('car-accessories/', CarAccessoryListView.as_view(), name='car-accessory-list'),
    path('car-accessories/<int:pk>/', CarAccessoryDetailView.as_view(), name='car-accessory-detail'),
    path('car-accessories/create/', CarAccessoryCreateView.as_view(), name='car-accessory-create'),  # Создание аксессуара
    path('car-accessories/<int:pk>/update/', CarAccessoryUpdateView.as_view(), name='car-accessory-update'),  # Редактирование аксессуара
    path('car-accessories/<int:pk>/delete/', CarAccessoryDeleteView.as_view(), name='car-accessory-delete'),  # Удаление аксессуара

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]