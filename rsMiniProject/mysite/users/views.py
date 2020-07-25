from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    form =UserCreationForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            Username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=User.objects.create_user(username=Username,password=password)
            user.save()
            messages.add_message(request, messages.SUCCESS,'New user created!')
            return redirect('polls:index')
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})
