"""
密码与用户名的校验规则
"""
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=50,
                               min_length=3,
                               required=True,
                               error_messages={'require':"用户名不能为空"})
    password = forms.CharField(max_length=50,
                               min_length=3,
                               required=True,
                               error_messages={'require': "密码不能为空"}
                               )