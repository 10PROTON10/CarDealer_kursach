from django.urls import path
from .views import home, CarsInStockView, favorite_page, profile_view, comparison_page, search_page

urlpatterns = [
    path('', home, name='home'),
    path('cars-in-stock/', CarsInStockView.as_view(), name='cars-in-stock'),
    path('favorites/', favorite_page, name='favorite-page'),
    path('profile/', profile_view, name='profile'),
    path('comparison/', comparison_page, name='comparison_page'),
    path('search/', search_page, name='search_page'),
    # Добавьте другие URL-пути для других разделов главной страницы, если необходимо
]



