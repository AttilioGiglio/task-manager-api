# Not use because there is no rendering, just an API
# from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # filter by an specific logged user and with data on datecompleted
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')



