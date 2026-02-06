from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import person_collection
from .form import personform
from bson import ObjectId

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
     person=list(person_collection.find())
     
     for p in person:
         p['id']=str(p["_id"]) #Create New Column 
         del p['_id']
         

     return render(request,'person_list.html',{'data':person})

def delete(request,id):
    person_collection.delete_one({"_id":ObjectId(id)})
    return redirect('person_list')

def edit(request,id):
    person=person_collection.find_one({"_id":ObjectId(id)})
    if request.method=="POST":
        form=personform(request.POST)
        if form.is_valid():
            data={
                'name': form.cleaned_data['name'],
                'mail': form.cleaned_data['mail'],
                'age': form.cleaned_data['age'],
            }

            person_collection.update_one(
                {"_id":ObjectId(id)},
                {"$set":data}
            )
            return redirect('person_list')
    else:
        form=personform(initial={
            "name":person["name"],
            "mail":person["mail"],
            "age":person["age"]
        })
        return render(request,'edit.html',{'form':form})
