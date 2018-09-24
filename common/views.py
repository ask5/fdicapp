from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from common.security import Security
from django.core.cache import cache

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('common:login')
    else:
        form = UserCreationForm()
    return render(request, 'common/app/sign_up.html', {'form': form})


def login_view(request):
    context = {}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.GET.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            security = Security()
            user_profile = security.get_user_profile(user)
            if user_profile:
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('web:home')
            else:
                return  redirect('common:unauthorized')
        else:
            context['error'] = "Incorrect Username or Password"

    return render(request, 'common/app/login.html', context)

def logout_view(request):
    security = Security()
    cache_key = security.cache_key(user=request.user)
    cache.delete(cache_key)
    logout(request)
    return redirect('common:login')

def unauthorized(request):
    return render(request, 'common/app/unauthorized.html', {})

