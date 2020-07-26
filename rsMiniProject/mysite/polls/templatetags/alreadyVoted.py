from django import template
from polls.models import Question, Choice


register=template.Library()

@register.filter
def alreadyVoted(value, CurrentUser):
    question= Question.objects.get(pk=value)
    voter_list=question.voters
    for userId in voter_list:
        if userId == CurrentUser:
            return False
    return True
