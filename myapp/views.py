from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from myapp.models import Dreamreal
from django.http import HttpResponse
import datetime

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
    # res = send_mail(
    #         'Dear Albertking',
    #         'Very Interesting',
    #         'infinite940714@outlook.com',
    #         [emailto],
    #         fail_silently=False,
    #     )
    # # res = send_mail('hello akira', 'what are you doing?', 'paul@polo.com', [emailto])
    # return HttpResponse('%s'%res)

# def crudops(request):
#     #Creating an entry

#     dreamreal = Dreamreal(
#         website = "www.polo.com", mail = "sorex@polo.com",
#         name = "sorex", phonenumber = '1234567890'
#     )
#     dreamreal.save()

#     #Read all entries
#     object = Dreamreal.objects.all()
#     res = "Printing all Dreamreal entries in the DB: <br>"

#     for elt in object:
#         res += elt.name + "<br>"

#     #Read a specific entry
#     sorex = Dreamreal.objects.get(name = 'sorex')
#     res += 'Printing One entry <br>'
#     res += sorex.name

#     #Delete an entry
#     res += '<br>Deleting an entry</br>'
#     sorex.delete()

#     #Update
#     dreamreal = Dreamreal(website = "www.polo.com", mail = "sorex@polo.com", 
#                           name = "sorex", phonenumber = '002376970')
#     dreamreal.save()
#     res += '<br>Updating an entry</br>'

#     dreamreal = Dreamreal.objects.get(name = 'sorex')
#     dreamreal.name = "thierry"
#     dreamreal.save()

#     return HttpResponse(res)