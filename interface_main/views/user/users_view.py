import json
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.shortcuts import render
from interface_main.utils.http_format import response_success
from  django.http import request
from interface_main.exception.my_exception import MyException
from interface_main.forms.user import UserForm
from interface_main.utils.log import default_log


# Create your views here.


class UsersView(View):

    def get(self, request, *args, **kwargs):
        """
        登录
        :param response:
        :param args:
        :param kwargs:
        :return:
        """
        form = UserForm(request.GET)
        result = form.is_valid() # 校验数据是否合法
        if not result:
            default_log.error(form.errors.as_json())
            raise MyException()

        user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        if user:
            login(request,user) # 登录持久化 ， 生成session
            return response_success('登录成功')
        else:
            raise MyException(message="登录失败")





    def post(self, request, *args, **kwargs):
        """
        注册
        :param response:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body #返回的是字符串
        data = json.loads(body) #把字符串解析为字典

        form = UserForm(data)
        result = form.is_valid()  # 校验数据是否合法
        if not result:
            default_log.error(form.errors.as_json())
            raise MyException()

        if User.objects.filter(username=form.cleaned_data['username']).exists():
            raise MyException(message='用户已存在')

        user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'])

        if user:
            login(request,user)
            return response_success("注册成功")
        else:
            raise MyException(message="注册失败")


    def delete(self,request,*args, **kwargs):
        """
        注销
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        login(request)
        return response_success("注销成功")




