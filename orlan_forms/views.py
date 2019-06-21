from django.shortcuts import HttpResponse
from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail

recipient_list = ["ilja.sonin2018@yandex.ru", "orlan-chechov@yandex.ru"]

def parent_form(request):
    if request.method == "POST":
        messagePost = request.POST
        subject = "Заявка на сайте orlan-chehov.ru"
        message = "Сообщение от {}\n\nEmail человека: {}\n\nМобильный телефон: {}\n\n{}".format(messagePost['name'],
                                                                                                messagePost['email'],
                                                                                                messagePost['phone'],
                                                                                                messagePost['message'])
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response

def contact_form(request):
    if request.method == "POST":
        messagePost = request.POST
        subject = "Заявка на сайте orlan-chehov.ru"
        message = "Сообщение от {}\n\nEmail человека: {}\n\nМобильный телефон: {}\n\n{}".format(messagePost['name'],
                                                                                                messagePost['email'],
                                                                                                messagePost['number'],
                                                                                                messagePost['message'])
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response

def phone_form(request):
    if request.method == "POST":
        messagePost = request.POST
        subject = "Заявка на сайте orlan-chehov.ru"
        message = "Кто-то хочет, чтобы вам перезвонили: {}".format(messagePost['phone'])
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        return HttpResponse('OK')
    else:
        response = render(request, '404.html')
        response.status_code = 404
        return response