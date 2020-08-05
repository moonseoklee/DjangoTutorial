from django.http import HttpResponseRedirect,HttpResponse,Http404

from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.views import View
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login,logout as auth_logout

def signUp(request):
    if request.method=='POST':
        signUpForm = UserCreationForm(request.POST)

        if signUpForm.is_valid():
            signUpForm.save()
        return HttpResponseRedirect('/login')
    else:
        signUpForm = UserCreationForm()
    return render(request,'login/signUp.html',{'signUpForm':signUpForm})

def login(request):
    loginError = None
    if request.method == 'POST':
        

        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
    
            return HttpResponseRedirect('/dashboard')
        else:
            loginError = '아이디,비밀번호 확인해주세요'

            
    else:
        loginForm = AuthenticationForm()
        
        
    
    
    return render(request, 'login/login.html', {'loginForm' : loginForm,'error':loginError})
    
    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login')
