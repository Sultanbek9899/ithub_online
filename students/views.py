from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserRegistrationForm, LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('my_courses_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
        # Сохраняем пользователя в базе данных.
            new_user.save()
            return render(request,
                          'register_done.html',
                           {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def log_out(request):
    logout(request)
    # Перенаправление на страницу.
    return redirect("courses_list")