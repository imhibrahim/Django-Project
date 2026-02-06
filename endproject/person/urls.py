from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('add/',views.insert),
    path('show/',views.fatch),
    path('person_list/',views.person_list,name='person_list'),
    path('form/',views.person_form,name='form'),
    path("del/<id>",views.delete,name="del"),
    path("edit/<id>",views.edit,name="edit")
]
