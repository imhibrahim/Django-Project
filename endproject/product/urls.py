from django.urls import path
from .import views
urlpatterns = [
    path('',views.fatchproduct),
    path('insertproduct',views.Insertproduct),
]
