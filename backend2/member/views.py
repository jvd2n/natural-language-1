from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes

from member.models import MemberVO
from member.serializers import MemberVOSerializer, LoginSerializer
from icecream import ic


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    if request.method == 'GET':
        ic('*****members(GET)*****')
        all_members = MemberVO.objects.all()
        ic(all_members)
        serializer = MemberVOSerializer(all_members, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        ic('****members(POST)*****')
        new_member = JSONParser().parse(request)
        ic(new_member)
        data = new_member['body']
        ic(data)
        serializer = MemberVOSerializer(data=data)
        ic(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        ic(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def member(request):
    if request.method == 'GET':
        ic('*****member(GET)*****')
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        ic('*****member(POST)*****')
        log_member = JSONParser().parse(request)
        ic(log_member)
        data = log_member['body']
        ic(data)
        ic(data['username'])
        auth_mem = get_object(data['username'])
        ic(auth_mem.password)
        # serializer = LoginSerializer(data=data)
        # ic(serializer.is_valid())
        if data['password'] == auth_mem.password:
            ic('*****password Authentication*****')
            return JsonResponse(
                {
                    'result': 'Welcome',
                    'username': data['username'],
                }, status=status.HTTP_200_OK)
        return JsonResponse('error')
    elif request.method == 'DELETE':
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)


def get_object(pk):
    try:
        return MemberVO.objects.get(pk=pk)
    except MemberVO.DoesNotExist:
        raise Http404
