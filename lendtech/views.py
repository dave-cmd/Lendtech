
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Transaction, MobileLoan, MobilePayment, BankLoan, BankPayment
from . forms import DateRangeForm
from itertools import chain
from datetime import datetime

# Create your views here

@login_required(login_url='login_page')
def home(request):
    mobile_payments = MobilePayment.objects.filter(user__pk=request.user.id).all()
    mobile_loans = MobileLoan.objects.all().filter(user__pk=request.user.id)
    bank_payments = BankPayment.objects.all().filter(user__pk=request.user.id)
    bank_loans = BankLoan.objects.all().filter(user__pk=request.user.id)
    
    loans, payments, totals = 0,0,0

    # Payments
    for item in mobile_payments:
        payments += item.amount
    
    for item in bank_payments:
        payments += item.amount

    # Loans
    for item in mobile_loans:
        loans += item.amount


    for item in bank_loans:
        loans += item.amount

    outstanding_loan = loans - payments
    transactions = Transaction.objects.all()

    context = {'transactions': transactions, 'loan': outstanding_loan}
    return render(request, 'lendtech/home.html', context=context)




@login_required(login_url='login_page')
def payments(request):
    return render(request, 'lendtech/payments.html')




@login_required(login_url='login_page')
def loans(request):

    context = { }
    if request.method == 'POST':

            date_format = "%m/%d/%Y"

            # mobile_loans = MobileLoan.objects.all().filter(created__range=[
            #     datetime.strptime(request.POST.get('start'), date_format), 
            #     datetime.strptime(request.POST.get('stop'), date_format)]
            # ).filter(user__pk=request.user.id).all().order_by('-created')


            # bank_loans = BankLoan.objects.all().filter(created__range=[
            #     datetime.strptime(request.POST.get('start'), date_format), 
            #     datetime.strptime(request.POST.get('stop'), date_format)]
            # ).filter(user__pk=request.user.id).all().order_by('-created')

            # context['transactions'] = list(chain(mobile_loans, bank_loans))

            context['transactions'] = Transaction.objects.all().filter(category='LOAN').filter(created__range=[
                datetime.strptime(request.POST.get('start'), date_format), 
                datetime.strptime(request.POST.get('stop'), date_format)]
            ).filter(user__pk=request.user.id).all().order_by('-created')

    else:

        # mobile_loans = MobileLoan.objects.all().filter(user__pk=request.user.id)
        # bank_loans = BankLoan.objects.all().filter(user__pk=request.user.id)
        # context['transactions'] = list(chain(mobile_loans, bank_loans))

        context['transactions'] = Transaction.objects.all().filter(category='LOAN')
        #[print(i.category) for i in context['transactions']]
    
    return render(request, 'lendtech/loans.html', context=context)




def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')
            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist.')

    context = {'page':'login'}
    return render(request, 'lendtech/login_register.html', context)




@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('home')
    


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured registering this user.')

    context = {'page':'register', 'form': form }
    return render(request, 'lendtech/login_register.html', context)
