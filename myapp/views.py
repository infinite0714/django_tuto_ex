from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from myapp.models import Dreamreal
from django.http import HttpResponse
import datetime
from myapp.forms import Loginform

# Create your views here.
def hello(request):
    today = datetime.datetime.now().date()

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "myapp/hello.html", {"today": today, "days_of_week": daysOfWeek})

def morning(request):
    text = "<h1>Good Morning!</h1>"
    return HttpResponse(text)

def article(request, articleID):
    text = "Displaying article Number : %s"%articleID
    # return HttpResponse(text)
    return redirect(articles, year = "2035", month = "02")

def articles(request, month, year):
    text = "Displaying articles of : %s/%s"%(month, year)
    return HttpResponse(text)

def sendSimpleEmail(request, emailto):
    email = EmailMessage("Dear Albert", "Interesting", 
                         "infinite940714@outlook.com", [emailto])
    fd = open('manage.py', 'r')
    email.attach('manage.py', fd.read(), 'text/plain')

    res = email.send()
    return HttpResponse('%s'%res)
def login(request):
    username = "not logged in"

    if request.method == 'POST':
        MyLoginForm = Loginform(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['user']
            
    else:
        MyLoginForm = Loginform()
    
    return render(request, 'myapp/loggedin.html', {"username": username})