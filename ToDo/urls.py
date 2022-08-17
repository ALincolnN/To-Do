from django.urls import path
from . import views
urlpatterns = [
    path('',views.list,name='lists'),
    path('insert',views.insert, name='insert'),
    path('delete/<int:todo_id>/',views.delete,name='delete')
]