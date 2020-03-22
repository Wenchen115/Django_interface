import traceback
from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin
from interface_main.utils.http_format import response_success,response_failed
from interface_main.exception.my_exception import MyException,ErrorCode

ALLOW_PATHS = ["/api/backend/user/info/","/api/backend/users/"]

class MyMiddleware(MiddlewareMixin):
    def process_request(self,request): #会捕捉所有的请求
        current_path = request.path
        if current_path in ALLOW_PATHS:
            pass
        else:
            user = request.user
            if user.is_authenticated:
                pass
            else:
                return response_failed(ErrorCode.COMMON,"用户未登录")

    def process_response(self,request,response): # 会捕捉所有的响应
        print("")
        return response

    def process_exception(self,request,exception): # 会捕捉所有的异常
        print(traceback.print_exc())
        if isinstance(exception,MyException): # isinstance：专门用来判断一个对象的类型
            print("这是我的错误")
            code = exception.code
            message = exception.message
            return response_failed(code, message)
        elif isinstance(exception,DatabaseError):
            print("数据库错误")
            return response_failed(ErrorCode.DB,"数据库错误")
        else:
            print("未知错误")
            return response_failed(ErrorCode.UNKNOWN,"未知错误")
