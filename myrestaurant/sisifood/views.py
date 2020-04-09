from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Pizza,Topping,Drink


# Create your views here.

def index(request):
    return render(request,'index.html',locals())

def pizza(request):
    if request.user.is_authenticated:
        pizza=Pizza.objects.all()
        return render(request, 'pizza.html',locals())
    else:
        return redirect("/home/login/")


def pizza_page(request,id):
    if request.user.is_authenticated:
        try:
            pizza = Pizza.objects.get(id=id)
        except Pizza.DoesNotExist:
            error = "Sorry, we don't have that kind of pizza now"
        return render(request, 'pizza_page.html', locals())
    else:
        return redirect("/home/login/")



def drink(request):
    return request(request,'drink.html',locals())

# def topping(request,name):
#     topping=Topping.objects.filter(name=name)
#     return request(request,'topping.html',locals())



def user_sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            first_name = sign_up_form.cleaned_data.get("first_name")
            last_name = sign_up_form.cleaned_data.get("last_name")
            username = sign_up_form.cleaned_data.get("username")
            phone_number= sign_up_form.cleaned_data.get("phone_number")
            password = sign_up_form.cleaned_data.get("password")
            email = sign_up_form.cleaned_data.get("email")
            user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/pizza/')
            else:
                error = "Please provide the correct password and username"
                sign_up_form = SignUpForm()
                return render(request, 'signup.html', locals())
    else:
        sign_up_form = SignUpForm()
        return render(request, 'signup.html', locals())





def user_logout(request):
    logout(request)
    return redirect("/home/login/")




def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/pizza/')
            else:
                error="Please provide the correct password and username"
                login_form = LoginForm()
                return render(request, 'login.html', locals())
    else:
        login_form = LoginForm()
    return render(request, 'login.html', locals())





