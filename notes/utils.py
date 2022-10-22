from rest_framework.response import Response
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


def get_notes(request):
    user = request.user
    notes = Note.objects.filter(user_id=user).order_by('-updated_at')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def get_note(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def add_note(request):
    data = request.data
    user = request.user
    note = Note.objects.create(
        user_id=User(id=user.id),
        title=data['title'],
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response(True)


def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(True)


def new_user(request):
    data = request.data
    new_user = User.objects.create(
        username=data['username'], email=data['email'], password=make_password(data['password']))
    new_user.save()
    return Response(True)
