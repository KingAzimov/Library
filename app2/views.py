from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def salomlash(request):
    return HttpResponse("Salom, loyihamizga xush kelibsiz!")

def ismlar(request):
    if request.user.is_authenticated:
        data={
            'my_name':"Abulhamdi",
            'names':["Ali","Ilhom","Javlon","Tohir","Saidahmad"]
        }
        return render(request, 'ismlar.html', data)
    else:
        return redirect('/')

def hamma_talabalar(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            Student.objects.create(
             ism=request.POST.get('st_name'),
             kitob_soni=request.POST.get('st_books')
            )
            return redirect('/students/')
        input_word = request.GET.get('st_name')
        if input_word is not None:
            talabalar = Student.objects.filter(ism__contains=input_word)
        else:
            talabalar = Student.objects.all()
        data={
            'students':talabalar
        }
        return render(request, 'all_students.html', data)
    else:
        return redirect('/')

def bitiruvchilar(request):
    if request.user.is_authenticated:
        data={
            'bitiruvchilar':Student.objects.filter(bitiruvchi=True)
        }
        return render(request, 'bitiruvchi.html', data)
    else:
        return redirect('/')

def kitob(request):
    if request.user.is_authenticated:
        data={
            'kitoblilar':Student.objects.filter(kitob_soni__gt=0)
        }
        return render(request, 'kitoblilar.html', data)
    else:
        return redirect('/')

def talaba_malumoti(request, son):
    if request.user.is_authenticated:
        data = {
            'student': Student.objects.get(id=son)
        }
        return render(request, 'student_data.html', data)
    else:
        return redirect('/')

def all_muallif(request):
    if request.user.is_authenticated:
        input_word=request.GET.get("st_ism")
        if input_word is not None:
            m=Muallif.objects.filter(ism__contains=input_word)
        else:
            m=Muallif.objects.all()
        data = {
            'mualliflar':m
        }
        return render(request, 'all_muallif.html',data)
    else:
        return redirect('/')

def muallif_malumoti(request, son):
    if request.user.is_authenticated:
        data = {
            'muallif': Muallif.objects.get(id=son)
        }
        return render(request, 'muallif_malumoti.html', data)
    else:
        return redirect('/')

def kitob_data(request, son):
    if request.user.is_authenticated:
        data = {
            'kitob': Kitob.objects.get(id=son)
        }
        return render(request, 'kitob_data.html', data)
    else:
        return redirect('/')

def sahifa(request):
    if request.user.is_authenticated:
        data={
            'big':Kitob.objects.all().order_by("-sahifa")[:3]
        }
        return render(request, 'bigsahifa.html', data)
    else:
        return redirect('/')

def janr(request):
    if request.user.is_authenticated:
        data={
            'janr':Kitob.objects.filter(janr='Komediya')
        }
        return render(request, 'kitob_janr.html', data)
    else:
        return redirect('/')

def kitob_soni(request):
    if request.user.is_authenticated:
        data={
            'kitob':Muallif.objects.filter(kitoblar_soni__gt=30).values("ism","kitoblar_soni")
        }
        return render(request, 'kitob_soni.html', data)
    else:
        return redirect('/')

def bitiruvchi(request):
    if request.user.is_authenticated:
        data={
            'bitiruvchi':Record.objects.filter(student__kitob_soni__gt=1)
        }
        return render(request, 'bitiuvchi_student.html', data)
    else:
        return redirect('/')

def student_ochirish(request, pk):
    if request.user.is_authenticated:
        Student.objects.get(id=pk).delete()
        return redirect("/students/")
    else:
        return redirect('/')

def hamma_kitoblar(request):
    if request.user.is_authenticated:
        input_word = request.GET.get('st_nom')
        if input_word is not None:
            kitob = Kitob.objects.filter(nom__contains=input_word)
        else:
            kitob = Kitob.objects.all()
        data={
            'kitoblar':kitob
        }
        return render(request, 'hamma_kitoblar.html', data)
    else:
        return redirect('/')

def hamma_record(request):
    if request.user.is_authenticated:
        input_word = request.GET.get('st_ism')
        if input_word is not None:
            st = Record.objects.filter(student__ism__contains=input_word)
        else:
            st = Record.objects.all()
        data={
            'students':st
        }
        return render(request, 'hamma_record.html', data)
    else:
        return redirect('/')

def muallif_delete(request, pk):
    if request.user.is_authenticated:
        Muallif.objects.get(id=pk).delete()
        return redirect("/mualliflar/")
    else:
        return redirect('/')

def loginview(request):
    if request.method=="POST":
        user=authenticate(username=request.POST.get('l'),password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request,user)
        return redirect('/kitoblar/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/')
    return render(request, 'register.html')