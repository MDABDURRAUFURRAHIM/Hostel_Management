from django.contrib import admin
from .models import Contactme
from .models import Account
from .models import Room
from .models import Seatcancle


# Register your models here.

# Contact Display 
@admin.register(Contactme)

class UserAdmin(admin.ModelAdmin):
    list_display=['name', 'stduentid','email','departnment','message']



#Account Display

@admin.register(Account)

class UserAdmin(admin.ModelAdmin):
    list_display=['name','stduentid','email','money','date','experieddate']



# Room Display

@admin.register(Room)

class UserAdmin(admin.ModelAdmin):
    list_display=['name','studentid','email','hallname','roomno','floorno']


# Seat Cancle Display

@admin.register(Seatcancle)

class UserAdmin(admin.ModelAdmin):
    list_display=['name','studentid','email','hallname','roomno']