from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm, newQuestionForm, givePerm
from .models import PollUser,Notify
from django.views import generic, View
from polls.models import Question,Choice,Comment

def register(request):
    form =UserRegisterForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            Username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            spirit_animal=form.cleaned_data.get('spirit_animal')
            user=PollUser.objects.create_user(username=Username,password=password, spirit_animal=spirit_animal)
            user.save()
            messages.add_message(request, messages.SUCCESS,'New user created! You can now log in.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

class ProfileView(View):
    template_name='users/profile.html'
    def get(self, request, user_id ):
        the_user=get_object_or_404(User,username=user_id)
        context={'the_user':the_user}
        return render(request, self.template_name, context)

    def post(self,request):
        pass

class MyPolls(View):
    template_name='users/mypolls.html'
    form_class=newQuestionForm
    def get(self, request, user_id ):
        the_user=get_object_or_404(User,username=user_id)
        form=self.form_class()
        context={'the_user':the_user, 'form':form}
        return render(request, self.template_name, context)

    def post(self,request,user_id):
        the_user=get_object_or_404(User,username=user_id)
        form=self.form_class(request.POST)
        context={'the_user':the_user, 'form':form}

        if form.is_valid():
            question_text=form.cleaned_data['question_text']
            choice1=form.cleaned_data['choice1']
            choice2=form.cleaned_data['choice2']
            description=form.cleaned_data['description']
            question=Question(user=request.user,question_text=question_text, description=description, voters=[])
            question.save()
            c1=Choice(question=question,choice_text=choice1)
            c2=Choice(question=question,choice_text=choice2)
            c1.save();c2.save()
            messages.add_message(request,messages.INFO,'Poll created!')
            return HttpResponseRedirect(request.path_info)

        return render(request, self.template_name, context)

class Notification(View):
    template_name='users/notification.html'
    form_class= givePerm
    def get(self,request,user_id):
        the_user=get_object_or_404(User,username=user_id)
        form=self.form_class()
        context={'the_user':the_user, 'form':form}
        return render(request, self.template_name,context)
    def post(self,request,user_id):
        the_user=get_object_or_404(User,username=user_id)
        form=self.form_class(request.POST)
        context={'the_user':the_user, 'form':form}
        if 'approve' in request.POST:
            #perm=form.cleaned_data['perm']
            print('approved')
            messages.add_message(request,messages.SUCCESS,'Change approved! New choice added to the question.')
            not_id=int(request.POST.get('thing')) #gets notification id
            choice_id=int(Notify.objects.get(id=not_id).not_memo)
            choice=Choice.objects.get(id=choice_id)
            choice.allowed=True
            choice.save()
            Notify.objects.get(id=not_id).delete()
            return HttpResponseRedirect(reverse('users:notification',args=(user_id,)))
        elif 'deny' in request.POST:
            print('denied')
            messages.add_message(request,messages.WARNING,'Change denied.')
            not_id=int(request.POST.get('thing')) #gets notification id
            Notify.objects.get(id=not_id).delete()
            return HttpResponseRedirect(reverse('users:notification',args=(user_id,)))
        elif 'markread' in request.POST:
            not_id=int(request.POST.get('thing')) #gets notification id
            status=Notify.objects.get(id=not_id)
            print(status)
            status.readStatus=True
            status.save()
        return render(request, self.template_name,context)
