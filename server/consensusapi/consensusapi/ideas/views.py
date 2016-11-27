from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from consensusapi.ideas.serializers import IdeaSerializer
from consensusapi.ideas.models import Idea



class IdeaViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents ideas.

    """
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all()
    
    
