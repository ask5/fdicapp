from django.shortcuts import render

def index(request):
    return render(request, 'www/pages/index.html')

def pricing(request):
    return render(request, 'www/pages/pricing.html')

def features(request):
    return render(request, 'www/pages/features.html')

def privacy(request):
    return render(request, 'www/pages/privacy.html')

def resources(request):
    return render(request, 'www/pages/resources.html')

def team(request):
    return render(request, 'www/pages/team.html')

def terms(request):
    return render(request, 'www/pages/terms.html')

def support(request):
    return render(request, 'www/pages/support.html')

def contact(request):
    return render(request, 'www/pages/contact.html')

