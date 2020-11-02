from django.contrib.auth import login, authenticate
from datetime import date
from django.shortcuts import render, redirect
from monolith.forms import BmiInputForm, SignUpForm, LoginForm, TellMeMoreForm
from monolith.classes import Bmi
from decimal import *
from django.contrib.auth.decorators import login_required

# Create your views here
from monolith.models import Profile, HistoricBmi

getcontext().prec = 4


@login_required(login_url='/login/')
def calculate_view(request):
    if request.method == 'POST':
        form = BmiInputForm(request.POST)
        if form.is_valid():
            new_bmi = Bmi(height=Decimal(request.POST['height']), weight=Decimal(request.POST['weight']))

            context = {
                'result': new_bmi.bmi(),
                'full_name': request.user.get_full_name(),
                'historic': HistoricBmi.objects.filter(user=request.user)
            }
            today = date.today()
            if not HistoricBmi.objects.filter(date=today):
                HistoricBmi.objects.create(user=request.user, bmi=new_bmi.bmi())
            else:
                context.update({'warning': 'We save only 1 bmi per day'})
            return render(request, 'bmi_result.html', context=context)
    else:
        form = BmiInputForm()
    context = {
        'name': request.user.get_full_name(),
    }
    return render(request, 'bmi_form.html', {'form': form, 'context': context})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('tell_me_more')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request, 'index.html', {})


def tell_me_more_view(request):
    if request.method == 'POST':
        form = TellMeMoreForm(request.POST)
        if form.is_valid():
            data = {
                'user': request.user,
                'birthday': form.cleaned_data.get('birthday'),
                'gender': form.cleaned_data.get('gender'),
                'condition': form.cleaned_data.get('condition'),
            }
            Profile.objects.create(**data)
            return redirect('calculate')
    else:
        form = TellMeMoreForm()
    return render(request, 'tell_me_more.html', {'form': form})