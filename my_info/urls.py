
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('account', views.account,name='account'),
    path('room', views.room,name='room'),
    path('seatcancle', views.seatcancle,name='seatcancle'),
    path('contactshowdata', views.contactshowdata,name='contactshowdata'),
    path('accountshowdata', views.accountshowdata,name='accountshowdata'),
    path('roomshowdata', views.roomshowdata,name='roomshowdata'),
    path('seatcancelshowdata', views.seatcancelshowdata,name='seatcancelshowdata'),

]