from django.shortcuts import render, HttpResponse
from django.http import HttpResponseForbidden

from .models import Reviews

def recive(request):
    if request.method == "POST":    
        try:    
            print(request.POST)
            
            reviews = Reviews()
            return HttpResponse('OK')
        except:
            return HttpResponseForbidden()
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response
        