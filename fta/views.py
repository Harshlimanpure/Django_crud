from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Reg
from .models import Form
# Create your views here.


def home(request):
    if request.method == 'POST':
        dbfm = Reg(request.POST)
        fm = Form(
            name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
        fm.save()
        dbfm = Reg()
    else:
        dbfm = Reg()
    stu = Form.objects.all()
    return render(request, 'home.html', {'form': dbfm, 'stu': stu})


def update(request, id):
    if request.method == 'POST':
        pi = Form.objects.get(pk=id)
        dbfm = Reg(request.POST, instance=pi)
        if dbfm.is_valid():
            dbfm.save()
    else:
        pi = Form.objects.get(pk=id)
        dbfm = Reg(instance=pi)
    return render(request, 'update.html', {'form': dbfm})


def delete(request, id):
    if request.method == 'POST':
        pi = Form.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    # return render(request, 'home.html',{'form':dbfm,'stu':stu})
    return HttpResponseRedirect('/')
