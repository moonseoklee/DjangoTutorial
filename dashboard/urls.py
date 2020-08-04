from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('',views.list,name='list'), 
    path('upload/',views.upload,name='upload'),
    path('<int:itemId>/',views.detail,name='detail'),
]