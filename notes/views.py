from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils import new_user, get_notes, get_note, add_note, update_note, delete_note


@api_view(['POST'])
def register_user(request):
    return new_user(request)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_add_notes(request):
    if request.method == 'GET':
        return get_notes(request)

    if request.method == 'POST':
        return add_note(request)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def query_notes(request, pk):
    if request.method == 'GET':
        return get_note(request, pk)

    if request.method == 'PUT':
        return update_note(request, pk)

    if request.method == 'DELETE':
        return delete_note(request, pk)
