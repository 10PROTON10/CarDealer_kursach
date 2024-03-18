from django.http import JsonResponse

from api.serializers import CarSerializer, FavoriteCarSerializer
from api.views import CarListView, SearchCarListView
from catalog.models import Brand, Favorite, Car  # Импортируйте модели, которые вам нужны из вашего проекта
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def home(request):
    brands = Brand.objects.all()

    context = {
        'brands': brands,
        'user': request.user,
    }

    return render(request, 'home.html', context)

class CarsInStockView(View):
    template_name = 'cars_in_stock.html'

    def get(self, request, *args, **kwargs):
        # Используем CarListView для получения списка машин
        car_list_view = CarListView.as_view()
        response = car_list_view(request)

        # Парсим JSON-данные из ответа
        cars_data = response.data

        return render(request, self.template_name, {'cars_data': cars_data})

def search_page(request):
    # Обработка запроса поиска машин
    if request.method == 'GET':
        # Используем CarListView для получения списка машин
        search_car_list_view = SearchCarListView.as_view()
        response = search_car_list_view(request)

        # Парсим JSON-данные из ответа
        search_cars_data = response.data

        # Передаем данные в контекст шаблона
        context = {
            'search_cars_data': search_cars_data,
        }

        # Отображаем шаблон search.html с данными о машинах
        return render(request, 'search.html', context)

@login_required(login_url='/auth/login/')
def favorite_page(request):
    favorite_cars = Favorite.objects.filter(user=request.user)
    context = {
        'favorite_cars': favorite_cars,
    }
    return render(request, 'favorites.html', context)

@login_required(login_url='/auth/login/')
def profile_view(request):
    # Получаем объект пользователя
    user_data = request.user

    # Передаем данные в контекст шаблона
    context = {
        'user_data': user_data,
    }

    # Отображаем шаблон с данными пользователя
    return render(request, 'profile.html', context)

@login_required(login_url='/auth/login/')
def comparison_page(request):
    # Получите все машины, выбранные для сравнения
    comparison_cars = Favorite.objects.filter(user=request.user, is_selected_for_comparison=True)

    context = {
        'comparison_cars': comparison_cars,
    }
    return render(request, 'comparison.html', context)

# class CarsInStockView(View):
#     template_name = 'cars_in_stock.html'
#
#     def get(self, request, *args, **kwargs):
#         api_url = 'http://127.0.0.1:8000/api/cars/'
#         response = requests.get(api_url)
#         cars_data = response.json()
#
#         return render(request, self.template_name, {'cars_data': cars_data})