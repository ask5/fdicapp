from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from common.decorators import subscription_required


@login_required
@subscription_required
def home(request):
    context = {}
    return render(request, 'web/pages/home.html', context)
