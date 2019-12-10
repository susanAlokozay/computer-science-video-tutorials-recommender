from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')

def register(request):
    return render(request, 'register.html')
def admission(request):
    return render(request, 'admission.html')
def courseDetail(request):
    return render(request, 'courseDetail.html')
def news(request):
    return render(request, 'news.html')


