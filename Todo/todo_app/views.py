from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def list_todo_items(request):
    todo_contents = Todo.objects.all()
    context = {'todo_list':  todo_contents}
    return render(request, 'todo/todo-list.html', context)

def list_item(request:HttpRequest):
    content = request.POST.get('content'," ")
    priority = request.POST.get('priority', " ")
    date = request.POST.get('date', '')
    if content:
        todo = Todo(
            content=content,
            priority=priority,
            date=date
        )
        todo.save()
        return redirect('list')
    else:
        return HttpResponse("failed to add")

def delete_item(request, todo_id):
    delete_item = Todo.objects.get(id=todo_id)
    delete_item.delete()
    return redirect('list')


def update_item(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(request.POST or None, request.FILES, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("todo:list")
    return render(request, 'todo/edit.html', {'form': form, 'movie': todo})


# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Todo
# from .forms import TodoForm

# class TodoListView(ListView):
#     model = Todo
#     template_name = 'todo/todo-list.html'
#     context_object_name = 'todo_list'

# class TodoCreateView(CreateView):
#     model = Todo
#     form_class = TodoForm
#     template_name = 'todo/todo-create.html'
#     success_url = reverse_lazy('list')

# class TodoUpdateView(UpdateView):
#     model = Todo
#     form_class = TodoForm
#     template_name = 'todo/todo-update.html'
#     success_url = reverse_lazy('list')

# class TodoDeleteView(DeleteView):
#     model = Todo
#     template_name = 'todo/todo-confirm-delete.html'
#     success_url = reverse_lazy('list')
