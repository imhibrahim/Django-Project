from django.shortcuts import render
from django.http import HttpResponse
from .form import productform
from django.core.files.storage import FileSystemStorage
import os,uuid
from .models import product_collection


def fatchproduct(request):
    return render(request,'product.html')

def Insertproduct(request):
    if request.method=="POST":
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            image_url= None
            if 'pic' in request.FILES:
                image=request.FILES['pic']
                ext=os.path.splitext(image.name)[1]
                new_name=f"{uuid.uuid4()}{ext}"
                fs=FileSystemStorage()
                filname=fs.save(new_name,image)
                image_url=fs.url(filname)
            data={
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'desc': form.cleaned_data['Description'],
                'pic': image_url
            }
            product_collection.insert_one(data)
            return HttpResponse("Data is Inserted....")
    else:
        form=productform()
        return render(request,'pinsert.html',{'productform':form})
