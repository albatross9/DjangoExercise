from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD
from Django.contirb.auth.hashers import make_password
=======
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD
>>>>>>> 회원가입창에 모든란에 항목을 안적었을떄 오류나오게
=======

>>>>>>> 로그인 세션 html, 뷰, urls 추가
from .models import Amsuser

# Create your views here.


def login(requset):
    if request.method == 'GET':
        return render(requset, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = '모든값을 입력!!'
        else:
            amsuser = Amsuser.objects.get(username=username)
            amsuser


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
<<<<<<< HEAD
                password=make_password(password)
=======
                useremail=useremail,
                password=password
>>>>>>> 이메일필드 추가
            )

            amsuser.save()

        return render(request, 'register.html', res_data)
