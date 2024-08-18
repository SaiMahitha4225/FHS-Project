from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import SignUpForm, RestaurantsForm, ManagerForm
from .models import SignUp, Admin, Restaurants, Manager


# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        formdata = SignUpForm(request.POST)
        if formdata.is_valid():
            formdata.save()

            msg="Successfully Registered"
            return render(request,"index.html",{"msg":msg})
        else:
            msg="Failed to register"
            return render(request,"signup.html",{"signupform":form,"msg":msg})
    return render(request,"signup.html",{"signupform":form})


def login(request):
    return render(request, "login.html")


"""def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["password"]

    flag = SignUp.objects.filter(Q(username=uname) & Q(password=pwd))
    print(flag)

    if flag:
        user = SignUp.objects.get(username=uname)
        print(user)
        print(user.id, user.fullname, user.gender)  # other fields also
        request.session["uname"] = user.username
        return render(request, "admin.html", {"uname": user.username})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})"""


def admin(request):

    return render(request,"admin.html")

def logout(request):
    return render(request,"login.html")
def adres(request):
    username = request.session["username"]
    form = RestaurantsForm()
    if request.method == "POST":
        formdata = RestaurantsForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "adres.html", {"username":username,"restaurantsform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "adres.html", {"username":username,"restaurantsform": form, "msg": msg})
    return render(request,"adres.html",{"username":username,"restaurantsform":form})

def addma(request):
    form = ManagerForm()
    if request.method == "POST":
        formdata = ManagerForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Employee Registered Successfully"
            return render(request, "addma.html", {"managerform": form,"msg":msg})
        else:
            msg = "Failed to Register Employee"
            return render(request, "addma.html", {"managerform": form, "msg": msg})
    return render(request,"addma.html",{"managerform":form})

def viewcus(request):
    return render(request, "viewcus.html")
def viewma(request):
    return render(request,"viewma.html")
def viewres(request):

    username=request.session["username"]

    restaurantslist = Restaurants.objects.all()

    return render(request,"viewres.html",{ "username": username,"restaurantslist":restaurantslist})

def cus(request):
    return render(request,"cus.html")

def cart(request):
    return render(request,"cart.html")


def delete(request,id):
    Cus.objects.filter(id=id).delete()
    return redirect("view")

"""def checklogin(request):
        username = request.POST["username"]
        password = request.POST["password"]

        flag = SignUp.objects.filter(Q(username=username) & Q(password=password))
        print(flag)

        if flag:
            user = SignUp.objects.get(username=username)
            print(user)
            print(user.id, user.username, user.gender)  # other fields also
            request.session["username"] = user.username
            return render(request, "cus.html", {"username": user.username})
        elif flag:
            admin = Admin.objects.get(username=username)
            print(admin)
            request.session["username"] = admin.username
            return render(request, "adminhome.html", {"useruname": admin.username})

        else:
            msg = "Login Failed"
            return render(request, "login.html", {"msg": msg})"""
def checklogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    flag = SignUp.objects.filter(Q(username=username) & Q(password=password))
    if username=="admin" and password=="admin":
        return redirect('admin')
    elif flag:
        user = SignUp.objects.get(username=username)
        print(user)
        print(user.id, user.username, user.gender)  # other fields also
        request.session["username"] = user.username
        return render(request, "cus.html", {"username": user.username})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})


def viewma(request):
    username=request.session["username"]
    managerlist = Manager.objects.all()
    count = Manager.objects.count()
    return render(request,"viewma.html",{"username":username,"managerlist":managerlist,"count":count})