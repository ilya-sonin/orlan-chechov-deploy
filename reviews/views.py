from django.shortcuts import render, HttpResponse
from django.http import HttpResponseForbidden

from .models import Reviews


def recive(request):
    if request.method == "POST":    
        try:
            review = Reviews.objects.create_obj(
                name=request.POST['name'],
                age=int(request.POST['age']),
                review=request.POST['review']
            )
            return HttpResponse('OK')
        except:
            return HttpResponseForbidden()
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response
        