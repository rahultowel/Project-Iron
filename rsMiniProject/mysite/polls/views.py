from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice, Comment
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from .forms import comForm
from django.contrib import messages

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(View):
    form_class=comForm
    template_name='polls/detail.html'

    def get(self,request,question_id,*args,**kwargs):

        template_name=self.template_name
        the_question= get_object_or_404(Question,id=question_id)
        comment_list=the_question.comment_set.all().order_by('-pub_date')
        form=self.form_class()
        context={'the_question':the_question,
        'form':form,'comment_list':comment_list}

        return render(request,template_name,context)

    def post(self,request,question_id,*args,**kwargs):

        template_name=self.template_name
        the_question= get_object_or_404(Question,id=question_id)
        comment_list=the_question.comment_set.all().order_by('-pub_date')
        form=self.form_class(request.POST)
        context={'the_question':the_question,
        'form':form,'comment_list':comment_list}

        if form.is_valid():
            #process data here
            this_comment=form.cleaned_data['this_comment']
            comment=Comment(user=request.user,question=the_question,comment_text=this_comment)
            comment.save()
            return HttpResponseRedirect(request.path_info)
        return render(request,template_name, context)


class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'
    context_object_name='the_question'

class testView(View):
    form_class=comForm
    template_name='polls/test.html'

    def get(self,request, *args, **kwargs):
        form = self.form_class()
        return render(request,self.template_name, {'form':form})

    def post(self,request,*args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            #process data here
            return HttpResponseRedirect(request.path_info)
        return render(request,self.template_name, {'form':form})

def vote(request,question_id):
    the_question= get_object_or_404(Question,id=question_id)
    try:
        selected_choice=the_question.choice_set.get(pk=request.POST['choice']) #name of the input tag
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {'the_question': the_question,
        'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        the_question.voters.append(request.user.id)
        the_question.save()
        selected_choice.save()
        messages.add_message(request,messages.SUCCESS,'Vote added')
        return HttpResponseRedirect(reverse('polls:results',args=(the_question.id,)))
