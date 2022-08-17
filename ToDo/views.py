from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import ToDo


# Create your views here.


def list(request):

    tasks = ToDo.objects.all()

    return render(request,'todos.html',{'tasks':tasks} )



def insert(request):

   
        todo = ToDo(content = request.POST['content'])
        todo.save()

        return redirect('/')
  

def delete(request,todo_id):

    
    rej= ToDo.objects.get(id=todo_id)
    rej.delete()

    return redirect('/')