from django.shortcuts import render,HttpResponse,redirect
from . import models
#from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    error_msg = ""
    if request.method == "POST":
        print(request.POST["email"])
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        if email == "admin@admin.cn" and pwd == "admin123":
            return redirect("/polls/user_list/")
        else:
            error_msg = "邮箱或密码错误"
    return render(request, "login.html", {"error": error_msg})

def user_list(request):
    ret = models.UserInfo.objects.all()
    print(ret[0].id, ret[0].name)
    return render(request, "user_list.html", {"user_list": ret})

def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("username", None)
        models.UserInfo.objects.create(name=new_name)
        return redirect("/polls/user_list/")
    return render(request, "add_user.html")