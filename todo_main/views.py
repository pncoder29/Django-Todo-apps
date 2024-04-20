from django.shortcuts import render
from todo.models import task
def home(request):
    utos = task.objects.filter(is_completed=False).order_by("-updated_at")
    
    #completed task
    completed_tasks= task.objects.filter(is_completed=True)
    context ={
        "utos":utos,
        "completed_tasks": completed_tasks,
    }
    return render(request, "index.html", context)