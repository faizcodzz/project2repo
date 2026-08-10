from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from . model import Task
# Create your views here.
def task_list(request):
    task = Task.objects.all().order_by('created_at')
    return render(request,'todo/task_list.html',{'task':task})


# def task_create(request):
#     if request,method =='POST':
#         title = request.POST.get('title','').strip()
#         description = request.POST.get('description','').strip()
#         if title:
#             Task.objects.create(title=title, description=description)