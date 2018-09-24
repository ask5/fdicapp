from django.shortcuts import render

def index(request):
    return render(request, 'provisioning/pages/index.html')