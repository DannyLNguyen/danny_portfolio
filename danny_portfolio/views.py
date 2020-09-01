from django.shortcuts import render, HttpResponse



def resume(request):
    return render(request, 'resume.html')


