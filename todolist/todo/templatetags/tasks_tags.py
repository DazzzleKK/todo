from django import template
from django.db.models import Count, F
from todo.models import Tasks

register = template.Library()


@register.simple_tag
def tasks_count():
    tasks_count = Tasks.objects.filter(completed__exact=False).count()    
    return tasks_count

@register.simple_tag
def completed_tasks_count():
    completed_tasks_count = Tasks.objects.filter(completed__exact=True).count()    
    return completed_tasks_count
