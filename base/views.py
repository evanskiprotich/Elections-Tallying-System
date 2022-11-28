from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ElectionResult

# Create your views here.


def home(request):
    return render(request, 'home.html')


def loginUser(request):
    return render(request, 'base/login.html')


@login_required(login_url='/login/')
def podashboard(request):
    
    if request.method == 'POST':
        officer = request.user
        candidate_one = request.POST['candidate_one']
        candidate_two = request.POST['candidate_two']
        candidate_three = request.POST['candidate_three']
        candidate_four = request.POST['candidate_four']
        totalvotes = request.POST['totalvotes']
        rejectedvotes = request.POST['rejectedvotes']
        validvotes = request.POST['validvotes']
        regvoters = request.POST['regvoters']

        results = ElectionResult(officer=officer, candidate_one = candidate_one, candidate_two = candidate_two, candidate_three = candidate_three, candidate_four = candidate_four, totalvotes = totalvotes, rejectedvotes = rejectedvotes, validvotes=validvotes, regvoters = regvoters)

        results.save()
        messages.success(request, 'Data has been submitted')

    return render(request, 'po_dashboard.html')

# login the user
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

# post results of an election with different candidates


#def electionPage(request):

    # if request.method == 'POST':
    #     candidate_one = request.POST['candidate_one']
    #     candidate_two = request.POST['candidate_two']
    #     candidate_three = request.POST['candidate_three']
    #     candidate_four = request.POST['candidate_four']
    #     totalvotes = request.POST['totalvotes']
    #     rejectedvotes = request.POST['rejectedvotes']
    #     validvotes = request.POST['validvotes']
    #     regvoters = request.POST['regvoters']

    #     results = ElectionResult.objects.create(candidate_one = candidate_one, candidate_two = candidate_two, candidate_three = candidate_three, candidate_four = candidate_four, totalvotes = totalvotes, rejectedvotes = rejectedvotes, validvotes=validvotes, regvoters = regvoters)

    #     results.save()


    # context = {}
    # return redirect(request, "home", context)


@login_required(login_url='/')
def custom_logout(request):
    logout(request)
    return redirect("home")

