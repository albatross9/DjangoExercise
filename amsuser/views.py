from .models import Amsuser
from Django.contirb.auth.hashers import make_password
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든값을 입력!!'
        else:
            amsusers = Amsuser.objects.get(username=username)
            if check_password(password, amsusers.password):
                pass
            else:
                res_data['error'] = '비번이 틀립니다!!!!!'

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            amsuser = Amsuser(
                username=username,
                password=make_password(password)
            )

            amsuser.save()

        return render(request, 'register.html', res_data)
