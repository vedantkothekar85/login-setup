from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.


@csrf_exempt
def test(request):
    var = request.POST.get('name')
    return JsonResponse({'var': var})


@csrf_exempt
def signup(request):
    return render(request, "signup.html")


@csrf_exempt
def signup_checkup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')

        send_data = New_signup(username=username, email=email,
                               dob=dob, password=password, conf_pass=conf_pass)
        if New_signup.objects.filter(email=email):
            return HttpResponse("exits")
        if len(password) == len(conf_pass) and password == conf_pass:
            send_data.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")


@csrf_exempt
def login(request):
    return render(request, 'login.html')


@csrf_exempt
def login_checkup(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not New_signup.objects.filter(email=email, password=password).exists():
        return HttpResponse('error')
    else:
        obj = New_signup.objects.get(email=email, password=password)
        request.session['user_id'] = str(obj.id)
        return HttpResponse('success')


@csrf_exempt
def dashboard(request):
    return HttpResponse("Dashboard")
