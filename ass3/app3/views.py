from django.shortcuts import render
from django.http import HttpResponse
from .models import Details
from .forms import Detailform
# Create your views here.
def create(request):
    if request.method =='POST':
        frm = Detailform(request.POST)
        if frm.is_valid():
            frm.save()
            frm = Detailform()

    else:
        frm=Detailform()
    data = Details.objects.all()
    return render(request, 'contact.html',{'form':frm , "data":data})
def Read(request):
    data=Details.objects.all()
    return render(request,'contact.html',{'data':data})
def update(request,d):
    a=Details.objects.get(Discription=d)
    va=Detailform(request.POST or None,instance=a)
    if va.is_valid():
        va.save()
        va=Details
    data = Details.objects.all()
    frm=Detailform()
    return  render(request,'contact.html',{'va':va, 'data':data, 'form':frm})
def delete(request,d):
    data = Details.objects.get(Discription=d)
    data.delete()
    read=Details.objects.all()
    return render(request,'contact.html',{'read':read})
