from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    print("about")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

