from django.shortcuts import render
from django.urls import path
# from . import views
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Member
from .serializers import MemberSerializer
from icecream import ic


class Auth(APIView):
    def get(self, request):
        ic(request)
        print('***** Save 1 ******')
        serializer = MemberSerializer(data=request)
        if serializer.is_valid():
            print('****** Save 2 ******')
            serializer.save()
        return Response({'result': 'WELCOME'})


# @csrf_exempt
# def member_list(request):
#     if request.method == 'GET':
#         member = Member.objects.all()
#         serializer = MemberSerializer(member, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MemberSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        serializer = MemberSerializer()
        if serializer.is_valid():

            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# class SignupAPI(generics.GenericAPIView):
#     serializer_class = CreateMemberSerializer()
#
#     def post(self, request, *args, **kwargs):
#         if len(request.data["username"]) < 6:
#             body = {'message': 'short field'}
#             return Response(body, status=status.HTTP_400_BAD_REQUEST)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(
#             {
#                 'user': MemberSerializer(
#                     user, context=self.get_serializer_context()
#                 ).data
#             }
#         )
