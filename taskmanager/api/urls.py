
from django.urls import path
from . import views

urlpatterns = [
    # todos
    path('todos', views.TodoCreateList.as_view()),
    path('todos/<int:pk>', views.TodoEditList.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
    #auth
    path('signup', views.signup),
    path('login', views.login)
]