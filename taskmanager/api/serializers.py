from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    class Meta:
        model = Todo
        # don't include user because It' not need it
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']