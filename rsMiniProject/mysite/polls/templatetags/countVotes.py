from django import template
from polls.models import Question, Choice

register=template.Library()

@register.filter
def countVotes(value):
    question= Question.objects.get(pk=value)
    choice_list=question.choice_set.all()
    votes=0
    for choice in choice_list:
        votes += choice.votes
    return votes
