from django.shortcuts import render,redirect
from .models import todo 
# Create your views here.
def index (request):
    Todo=todo.objects.all()
    if request.method== "POST":
        new_todo = todo( 
            title=request.POST["title"]


        )
        new_todo.save()
        return redirect('/')

    return render(request,'index.html',{"Todo":Todo})
def delete(request,pk):
    Todo=todo.objects.get(id=pk)
    Todo.delete()
    return redirect('/')