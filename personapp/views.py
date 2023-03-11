from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
# Create your views here.

def person_list(request):
    records=Person.objects.all()
    mydict={'records':records}
    return render(request,'Listingpage.html',context=mydict)

def AddPerson(request):
    mydict={}
    form=PersonForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    mydict['form']=form
    return render(request,'Add.html',mydict)

def EditPerson(request,id=None):
    one_rec=Person.objects.get(pk=id)
    form=PersonForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict= {'form':form}
    return render(request,'Edit.html',context=mydict)
def DeletePerson(request,eid=None):
    one_rec = Person.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('/')
    return render(request,'Delete.html')
def ViewPerson(request,eid=None):
    mydict={}
    one_rec = Person.objects.get(pk=eid)
    mydict['person']=one_rec
    return render(request,'''View.html''',mydict)