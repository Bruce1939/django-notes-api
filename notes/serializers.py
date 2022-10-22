from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        # fields = ['title', 'body']  #field specific serialization
