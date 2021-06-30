from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer
from icecream import ic


class Posts(APIView):
    def post(self, request):
        data = request.data['jsonData']
        ic(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'{serializer.data.get("title")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)
