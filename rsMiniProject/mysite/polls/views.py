from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')
    context ={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    #the_question=Question.objects.get(id=question_id)
    the_question= get_object_or_404(Question,id=question_id)
    context={'the_question':the_question}
    return render(request,'polls/detail.html',context)

def results(request, question_id):
    the_question= get_object_or_404(Question,id=question_id)
    context={'the_question':the_question}
    return render(request,'polls/results.html',context)

def vote(request,question_id):
    the_question= get_object_or_404(Question,id=question_id)
    try:
        selected_choice=the_question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {'the_question': the_question,
        'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save() 
        return HttpResponseRedirect(reverse('polls:results',args=(the_question.id,)))
