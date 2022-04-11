from django.http import HttpResponse
from django.shortcuts import render
from .models import Contactme, Seatcancle
from .models import Account
from .models import Room
from .models import Seatcancle 


# Create your views here.

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        studentid = request.POST.get('studentid')
        email = request.POST.get('email')
        departnment = request.POST.get('departnment')
        message = request.POST.get('message')

        contacts = Contactme()
        contacts.name = name
        contacts.stduentid = studentid
        contacts.email = email
        contacts.departnment = departnment 
        contacts.message = message
        contacts.save()
        return HttpResponse('<h1>Thanks for contacting us.<h1>')

    return render(request,'contact.html')





def contactshowdata(request):
    contactshow = Contactme.objects.all()
    contactshowdata = {'Contactme':contactshow}
    return render(request,'contactshowdata.html',contactshowdata)






#ACCOUNT PAGE :

def account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        studentid = request.POST.get('studentid')
        email = request.POST.get('email')
        money = request.POST.get('money')
        date = request.POST.get('date')
        experieddate = request.POST.get('experieddate')

        accounts = Account()
        accounts.name = name
        accounts.stduentid = studentid
        accounts.email = email
        accounts.money=  money 
        accounts.date = date
        accounts.experieddate = experieddate
        accounts.save()
        return HttpResponse('<h1>Thanks for the payment. <h1>')
    return render(request,'account.html')




#Accound Show Data 

def accountshowdata(request):
    accountshow = Account.objects.all()
    accountshowdata = {'Account':accountshow}
    return render(request,'accountshowdata.html',accountshowdata)



# Room informetation

def room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        studentid = request.POST.get('studentid')
        email = request.POST.get('email')
        hallname = request.POST.get('hallname')
        roomno = request.POST.get('roomno')
        floorno = request.POST.get('floorno')

        rooms = Room()
        rooms.name = name
        rooms.studentid = studentid
        rooms.email = email
        rooms.hallname =  hallname 
        rooms.roomno = roomno
        rooms.floorno = floorno
        rooms.save()
        return HttpResponse('<h1>Thanks for admitting here. <h1>')
    return render(request,'room.html')


#Room Showdata Tabil

def roomshowdata(request):
    roomshow = Room.objects.all()
    roomshowdata = {'Room': roomshow}
    return render(request,'roomshowdata.html',roomshowdata)








# Sit Cancle Information

def seatcancle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        studentid = request.POST.get('studentid')
        email = request.POST.get('email')
        hallname = request.POST.get('hallname')
        roomno = request.POST.get('roomno')
        
        seatcancel = Seatcancle()
        seatcancel.name = name
        seatcancel.studentid = studentid
        seatcancel.email = email
        seatcancel.hallname =  hallname 
        seatcancel.roomno = roomno
        seatcancel.save()
        return HttpResponse('<h1>Your seat has been cancelled. <h1>')
    return render(request,'seatcancle.html')
    

# Seat Cancel Show Data:


def seatcancelshowdata(request):
    seatcancelshow = Seatcancle.objects.all()
    seatcancelshowdata = {'Seatcancle': seatcancelshow}
    return render(request,'seatcancelshowdata.html',seatcancelshowdata)

