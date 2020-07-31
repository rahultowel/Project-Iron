from django import template
from users.models import Notify
from django.contrib.auth.models import User

register=template.Library()

@register.filter
def unread(value):
    user=User.objects.get(id=value)
    return user.notify_set.all().filter(readStatus=False).count()
