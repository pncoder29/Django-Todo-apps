from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import task

# Create your views here.
def addTask(request):
    task01 = request.POST["task"]
    task.objects.create(task=task01)
    return redirect("home")

def mark_as_done(request, pk):
    task02 = get_object_or_404(task, pk=pk)
    task02.is_completed = True 
    task02.save()
    return redirect("home")

