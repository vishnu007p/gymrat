
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from . models import *

def first(request):
    return render(request,'index.html') 

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def classtime(request):
    return render(request,'classtime.html')

def packages(request):
    return render(request,'packages.html')

def sections(request):
    return render(request,'sections.html')

def section(request):
    return render(request,'sections.html')

def register(request):
    return render(request,'register.html')

def userlogin(request):
    uemail = request.POST.get('uemail')
    upassword = request.POST.get('upassword')
    if uemail == 'ad@ad' and upassword =='ad':
        request.session['logintdetail'] = uemail
        request.session['admin'] ='admin'
        return render(request,'index.html')

    elif users.objects.filter(uemail=uemail,upassword=upassword).exists():
        udetail=users.objects.get(uemail=request.POST['uemail'],upassword=upassword)
        if udetail.upassword == request.POST['upassword']:
            request.session['uid'] = udetail.id
            request.session['uname'] = udetail.uname

            request.session['uemail'] = uemail

            request.session['user'] = 'user'

            
            return render(request,'userdetails.html')

    else:
            return render(request, 'login.html', {'status': 'failed'})

def userreg(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        uemail=request.POST.get('uemail')
        upassword=request.POST.get('upassword')
        uaim=request.POST.get('uaim')
        log=users(uname=uname,uemail=uemail,upassword=upassword,uaim=uaim)
        log.save()
        return redirect(userlogin)
    return render(request,'register.html')

def udetails(request):
    varr=request.session['uid']
    if request.method=='POST':
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        age=request.POST.get('age')
        a=int(weight)
        b=int(height)
        c=a/(b/100)**2
        if (c>18.5 and c<25):
            x='normal'
        elif (c<18.5):
            x='underweight, lets try to make it!!'
        else:
            x='overweight,  lets try to make it!!'
        log=udetail(varr=varr,weight=weight,height=height,age=age,bmi=c,status=x)
        log.save()
        return redirect(proview)
    return render(request,"userdetails.html")

def pro(request):
    return render(request,'profile.html')

def proview(request):
    temp=request.session['uid']
    proshow=udetail.objects.get(varr=temp)
    return render(request,'profile.html',{'res':proshow})


def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def login(request):
    return render(request,'login.html')

def trainers(request):
    return render(request,'trainers.html')

def profile(request):
    return render(request,'profile.html')

def payments(request):
    return render(request,'payment.html')

def product(request):
    return render(request,'products.html')

def packageselect(request):
    return render(request,'packageselect.html')






 