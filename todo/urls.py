from django.urls import path
from . import views

urlpatterns = [
    #add task
    path("addTask/", views.addTask, name="addTask"),
    
    #this for button mark as done going to complete task
    path('mark_as_done/<int:pk>/', views.mark_as_done, name="mark_as_done"),
    
    #this for mark undone task
    # path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),
    
    #this for Edit features
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task"),
    
    #this is for Delete task
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
]