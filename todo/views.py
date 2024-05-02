from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import task

# Create your views here.
def addTask(request):
    task01 = request.POST["task"]
    task.objects.create(task=task01)
    return redirect("home")

#this for button of mark as done
def mark_as_done(request, pk):
    task02 = get_object_or_404(task, pk=pk)
    task02.is_completed = True 
    task02.save()
    return redirect("home")


#this for Edit task Features
def edit_task(request, pk):
    get_task = get_object_or_404(task, pk=pk)
    if request.method == "POST":
        #targeting the <input type name"task">
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:
        context ={
            "get_task":get_task,
        }
    return render(request, "edit_task.html", context)

#This for delete task features
def delete_task(request, pk):
    task02 = get_object_or_404(task, pk=pk)
    task02.delete()
    return redirect("home")
    



























