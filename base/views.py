from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Result, Candidate
<<<<<<< HEAD
from django.db.models import Sum, Avg, F, Count
from django.db.models.functions import Round
=======
from django.db.models import Sum, Avg, F
>>>>>>> 2aa10f91a002768e3804ab163ed566bed639d8d3

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


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

        results = Result(officer=officer, candidate_one = candidate_one, candidate_two = candidate_two, candidate_three = candidate_three, candidate_four = candidate_four, totalvotes = totalvotes, rejectedvotes = rejectedvotes, validvotes=validvotes, regvoters = regvoters)

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


def view_candidates(request, candidate_id):
    candidate_list = Candidate.objects.all(pk=candidate_id)
    
    return render(request, 'home.html',
                    {'candidate': candidate_list})


def view_result(request):
    results = Result.objects.all()

    
    return render(request, 'base/results.html',
                    {'results': results})


def view_candidate(request):
    candidates = Candidate.objects.all()
    
    context = {
    "candidates": candidates,
    } 
    
    return render(request, 'base/results.html',
                    context)

def view_result(request):
    constituencies = len(Result.objects.all())
    candidateOne = Result.objects.all().aggregate(Sum(F('candidate_one')))
    candidateTwo = Result.objects.all().aggregate(Sum('candidate_two'))
    candidateThree = Result.objects.all().aggregate(Sum('candidate_three'))
    candidateFour = Result.objects.all().aggregate(Sum('candidate_four'))
    totalvotes = Result.objects.all().aggregate(Sum(F('totalvotes')))
    rejectedvotes = Result.objects.all().aggregate(Sum('rejectedvotes'))
    validvotes = Result.objects.all().aggregate(Sum('validvotes'))
    regvoters = Result.objects.all().aggregate(Sum('regvoters'))

    #percentages
<<<<<<< HEAD
    candidate1 = (list(Result.objects.aggregate(Sum('candidate_one')).values())[
        0] / list(Result.objects.aggregate(Sum('totalvotes')).values())[0])* 100
    first_candidate = float(candidate1)
    candidate2 = (list(Result.objects.aggregate(Sum('candidate_two')).values())[
        0] / list(Result.objects.aggregate(Sum('totalvotes')).values())[0]) * 100
    candidate3 = (list(Result.objects.aggregate(Sum('candidate_three')).values())[
        0] / list(Result.objects.aggregate(Sum('totalvotes')).values())[0]) * 100
    candidate4 = (list(Result.objects.aggregate(Sum('candidate_four')).values())[
        0] / list(Result.objects.aggregate(Sum('totalvotes')).values())[0]) * 100
    turnOut = (list(Result.objects.aggregate(Sum('totalvotes')).values())[
        0] / list(Result.objects.aggregate(Sum('regvoters')).values())[0]) * 100
=======
    candidate1 = Result.objects.aggregate(Avg('candidate_one'))
    # candidate2 = (candidateTwo/totalvotes)*100
    # candidate3 = (candidateThree/totalvotes)*100
    # candidate4 = (candidateFour/totalvotes)*100
    # turnOut = (totalvotes/regvoters)*100 
>>>>>>> 2aa10f91a002768e3804ab163ed566bed639d8d3

    context = {
    "constituencies": constituencies,
    "candidateOne": candidateOne,
    "candidateTwo": candidateTwo,
    "candidateThree": candidateThree,
    "candidateFour": candidateFour,
    "totalvotes": totalvotes,
    "rejectedvotes": rejectedvotes,
    "validvotes": validvotes,
    "regvoters": regvoters, 
    "candidate1": candidate1,
<<<<<<< HEAD
    "candidate2": candidate2,
    "candidate3": candidate3,
    "candidate4": candidate4,
    "turnOut": turnOut,
=======
    # "candidate2": candidate2,
    # "candidate3": candidate3,
    # "candidate4": candidate4,
    # "turnOut": turnOut,
>>>>>>> 2aa10f91a002768e3804ab163ed566bed639d8d3
    }

    return render(request, 'base/results.html',
                    context)