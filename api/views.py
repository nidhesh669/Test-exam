from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permisson import IsOwnerOfObject
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from django.contrib.auth.models import User

class TodoAPIView(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOfObject,IsAuthenticated,)
	authentication_classes = [BasicAuthentication,TokenAuthentication]
	def get_queryset(self):
		return Todo.objects.filter(users=self.request.user)
	serializer_class=TodoSerializer


class TodoAPIViews(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOfObject,IsAuthenticated,)
	authentication_classes = [BasicAuthentication,TokenAuthentication]
	def get_queryset(self):
		return Todo.objects.filter(users=self.request.user)
	serializer_class=TodoSerializer


    
from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Todo.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)