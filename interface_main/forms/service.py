"""
密码与用户名的校验规则
"""
from django import forms

class ServiceForm(forms.Form):
    name = forms.CharField(max_length=200,
                               min_length=1,
                               required=True,
                               error_messages={'require':"name can not be empty"})
    description = forms.CharField(max_length=2000,
                               min_length=1,
                               required=True,
                               error_messages={'require': "description can not be empty"}
                               )
    parent = forms.IntegerField(required=False)