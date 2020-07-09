from django.shortcuts import render, HttpResponse


def landing(request):
    return render(request, "welcome.html")

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')