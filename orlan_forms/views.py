from django.shortcuts import HttpResponse
from django.shortcuts import render 

def parent_form(request):
    if request.method == "POST":
        print(request)
        print(request.POST)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response

def contact_form(request):
    if request.method == "POST":
        print(request)
        print(request.POST)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response

def phone_form(request):
    if request.method == "POST":
        print(request)
        print(request.POST)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response