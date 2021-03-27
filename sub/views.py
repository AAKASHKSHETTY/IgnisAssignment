from django.shortcuts import render, redirect
from sub.models import *


def home(request):
    data = camp.objects.all()
    context = {'data': data,}
    if request.method == 'POST':
        bool = request.POST.get('bool')
        if bool == 'False':
            camp.objects.filter(event_name=request.POST.get('title')).update(is_liked= 1)
        else:
            camp.objects.filter(event_name=request.POST.get('title')).update(is_liked = 0)
    return render(request, 'home.html',context)

def enter(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        date = request.POST.get('lname')
        time = request.POST.get('time')
        loc = request.POST.get('loc')
        pictures = request.FILES.get('pictures')
        list = camp(event_name=name, date=date, time=time ,location=loc,is_liked = 0,img=pictures)
        list.save()
        return redirect('home')
    return render(request, 'enter.html')

