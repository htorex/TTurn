from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

from products.models import Product

from .forms import RegisterForm
from usersdate.models import User


def index(request):

    products = Product.objects.all()

    return render(request, 'index.html',{'message': 'Listado', 'tittle': 'fecha',
                                         'products' : products})


def login_view(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "bienvenido {}".format(User.username))
            return redirect('index')

        else:
            messages.error(request, "username o contraseña no validos")

    return render(request, 'users/login.html')
    

def logout_view(request):

    logout(request)
    messages.success(request, "Sesion Cerrada con Exito")
    return redirect('login')

def register(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST'and form.is_valid():
        
        user = form.save()
        
        if user:
            login(request, user)
            messages.success(request, "se ha registrado de manera exitosa")
            return redirect("index")

    return render(request, 'users/register.html', {
        'form' : form
    })