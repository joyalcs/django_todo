from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_todo_items, name='list'),
    path('insert_todo/',views.list_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>', views.delete_item, name='delete_item'),
    path('update/<int:todo_id>', views.update_item, name='update_item'),
    # path('list/',views.TodoListView.as_view(), name='list'),
    # path('insert_todo/',views.TodoCreateView.as_view(), name='insert_todo_item'),
    # # path('delete_todo/<int:todo_id>', views.TodoDeleteView.as_view(), name='delete_item'),
    # # path('update/<int:todo_id>', views.TodoUpdateView.as_view(), name='update_item')
    # path('update/<int:todo_id>/', TodoUpdateView.as_view(), name='todo-update'),  # Example with primary key
    # path('delete/<slug:slug>/', TodoDeleteView.as_view(), name='todo-delete'),,
]

