from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def loginUser(request):
    return render(request, 'base/login.html')

@login_required(login_url='/login/')
def podashboard(request):
    return render(request, 'po_dashboard.html')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('podashboard')
        else:
            messages.error(request, "User does not exist")




    context = {}
    return render(request, 'base/login.html', context)


@login_required(login_url='/')
def custom_logout(request):
    logout(request)
    return redirect("home")