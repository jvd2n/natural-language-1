from django.shortcuts import render
from django.urls import path
# from . import views
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Member
from .serializers import CreateUserSerializer, MemberSerializer, MemberCreateSerializer
from icecream import ic
from knox.models import AuthToken


class Connection(APIView):
    def get(self, request):
        return Response({'connection': 'testtttt'})

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


@api_view(['POST'])
@permission_classes([AllowAny])
def createMember(request):
    if request.method == 'POST':
        serializer = MemberCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if Member.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


class MemberCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (AllowAny, )


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)
            }
        )


class Auth(APIView):
    def post(self, request):
        ic(request)
        print('***** Save 1 ******')
        serializer = MemberSerializer(data=request.data)
        ic(serializer)
        ic(request.data)
        ic(request.method)
        data = JSONParser().parse(request.data)
        # ic(data)
        ic(serializer.is_valid())
        if serializer.is_valid():
            print('****** Save 2 ******')
            serializer.save()
        return Response({'result': 'WELCOME'})


@csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
def member_list(request):
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        ic('******POST*******')
        # ic(request.META)
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            ic('*****save*****')
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def member_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     ic(request)
#     if request.method == 'GET':
#
#         serializer = MemberSerializer()
#         if serializer.is_valid():
#
#             serializer.save()
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MemberSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


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
