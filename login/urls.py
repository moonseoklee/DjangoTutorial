from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('signUp/',views.signUp,name='signUp'),
    path('logout/',views.logout,name='logout')
    
]