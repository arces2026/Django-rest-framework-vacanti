from django.shortcuts import render
from rest_framework import viewsets
from .models import Libro, Autore
from .serializers import AutoreSerializer, LibroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profilo(request):
    return Response({
        'username': request.user.username,
        'user_id': request.user.id
    })

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticated]



class AutoreViewSet(viewsets.ModelViewSet):
    queryset = Autore.objects.all()
    serializer_class = AutoreSerializer
    permission_classes = [IsAuthenticated]