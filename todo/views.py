from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from . model import Task
# Create your views here.
def task_list(request):
    task = Task.objects.all().order_by('created_at')
    return render(request,'todo/task_list.html',{'task':task})


def task_create(request):
    if request,method =='POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        if title:
            Task.objects.create(title=title, description=description)
            return redirect(reverse('todo:task_list')) # it redirects to the todo:task_list page
        error = 'title cannot be empty'
        return render (request,'todo/task_form.html',{'error':error})
    return render(request,'todo/task_form.html')

def task_update(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request,method =='POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        completed = request.POST.get('completed')=='on'
        if title:
            task.title=title
            task.description=description
            task.completed=completed
            task.save()
            return redirect(reverse('todo:task_list'))
