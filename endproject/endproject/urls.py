"""
URL configuration for endproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from endproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/',include('person.urls')),
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('course/',views.course,name="course"),
    path('detail/',views.detail,name="detail"),
    path('price/',views.price,name="price"),
    path('start/',views.start,name="start"),
    path('train/',views.train,name="train"),
    path('event/',views.event,name="event"),
    path('adminpage/',views.adminindex,name="adminpage"),
    path('user/',views.user,name="user"),
]
