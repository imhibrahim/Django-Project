from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import person_collection
from .form import personform

def index(request):
    return HttpResponse("Data Base Is connected")

def insert(request):
    record={
        "firstName":"Muhammad Ibrahim",
        "LastName":"Afzal Ahmed",
        "Mail":"ibrahim@gmail.com"
    }
    person_collection.insert_one(record)
    return HttpResponse("Data Is Inserted.......")


def fatch(reqest):
    person=person_collection.find()
    return HttpResponse(person)


def person_form(request):
    if request.method=="POST":
        form=personform(request.POST)
        if form.is_valid():
            data={
                'name': form.cleaned_data['name'],
                'mail': form.cleaned_data['mail'],
                'age': form.cleaned_data['age'],
            }
            person_collection.insert_one(data)
            return redirect('person_list')
    else:
        form=personform()
        return render(request,'form.html',{'form':form})

    
def person_list(request):
     person=person_collection.find()
     return render(request,'person_list.html',{'data':person})