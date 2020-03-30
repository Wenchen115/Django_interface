import json

from django.forms import model_to_dict
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.shortcuts import render
from interface_main.utils.http_format import response_success
from  django.http import request
from interface_main.exception.my_exception import MyException
from interface_main.forms.user import UserForm
from interface_main.utils.log import default_log
from interface_main.models.service import Service
from interface_main.forms.service import ServiceForm





class ServiceDetailView(View):

    def get(self, request,service_id, *args, **kwargs):
        """
        获取单个服务
        :param response:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first() # 获取的是一个单个数据
        if service is None:
            return response_success()
        else:
            return response_success(model_to_dict(service)) # 转成字典返回


    def put(self, request,service_id, *args, **kwargs):
        """
        更新服务
        :param response:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first()
        if service is None:
            return response_success()

        body = request.body

        if not body:
            return response_success()
        data = json.load(body)
        form = ServiceForm(data)

        if form.is_valid():
            # Service.objects.filter(id=service_id).update(name=form.cleaned_data["name"],
            #                                              description=form.cleaned_data["description"],
            #                                              parent=form.cleaned_data["parent"])
            Service.objects.filter(id=service_id).update(**form.cleaned_data)
            return response_success()
        else:
            raise MyException()



    def delete(self, request,service_id, *args, **kwargs):
        """
        删除服务
        :param response:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        Service.objects.filter(id=service_id).delete()
        return response_success()



