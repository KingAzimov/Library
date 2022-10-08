from django.contrib import admin
from django.urls import path
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('ismlar/', ismlar),
    path('students/', hamma_talabalar),
    path('bitiruvchi/', bitiruvchilar),
    path('kitoblilar/', kitob),
    path('student/<int:son>/', talaba_malumoti),
    path('mualliflar/', all_muallif),
    path('muallif/<int:son>/', muallif_malumoti),
    path('kitob_data/<int:son>/', kitob_data),
    path('sahifa/',sahifa),
    path('janr/',janr),
    path('kitob_soni/',kitob_soni),
    path('bit/',bitiruvchi),
    path('student_ochir/<int:pk>/', student_ochirish),
    path('kitoblar/', hamma_kitoblar),
    path('records/', hamma_record),
    path('', loginview),
    path('logout/', logoutview),
    path('register/', register),
    path('muallif_delete/<int:pk>/', muallif_delete),
]