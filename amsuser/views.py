from django.http import HttpResponse
from django.shortcuts import render
from .models import Amsuser

# Create your views here.


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            amsuser = Amsuser(
                username=username,
                password=password
            )

            amsuser.save()

        return render(request, 'register.html', res_data)
