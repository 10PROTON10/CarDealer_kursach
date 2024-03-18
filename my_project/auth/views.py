from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу после успешного входа
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/register.html', {'form': form})

def logout_view(request):
    # Удаляем пользователя из сессии
    logout(request)

    # Если необходимо, удаляем все переменные сессии
    request.session.flush()
    response = redirect('home')
    response.delete_cookie('refresh_token')
    response.delete_cookie('access_token')

    # Удаляем пользователя из объекта запроса
    if hasattr(request, 'user'):
        request.user = None

    return response
