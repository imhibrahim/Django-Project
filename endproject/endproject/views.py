from django.shortcuts import render

def index(request):
    return render(request,'user/index.html')

def about(request):
    return render(request,'user/about.html')
def contact(request):
    return render(request,'user/contact.html')
def event(request):
    return render(request,'user/events.html')
def course(request):
    return render(request,'user/courses.html')
def detail(request):
    return render(request,'user/course-details.html')
def price(request):
    return render(request,'user/pricing.html')
def start(request):
    return render(request,'user/starter-page.html')
def train(request):
    return render(request,'user/trainers.html')

def adminindex(request):
    return render(request,"admin/index.html")


def user(request):
    return render(request,"admin/user.html")