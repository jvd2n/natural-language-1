from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberVOSerializer
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
import json


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberVOSerializer(all_members, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberVOSerializer(data = new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result':f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def member(request):
    if request.method == 'GET':
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        ic('******POST******')
        data = request.data['body']
        ic(data)
        pk = data['username']
        ic(pk)
        user_input_password = data['password']
        ic(user_input_password)
        # member = self.get_object(pk)
        try:
            member = MemberVO.objects.get(pk=pk)
            ic(member)
            if user_input_password == member.password:
                ic('***** pwd TRUE *****')
                serializer = MemberVOSerializer(member, many=False)
                # return JsonResponse({'result': 'SUCCESS', 'username': data['username']}, status=201)
                ic(serializer.data)
                return JsonResponse(data=serializer.data, safe=False)
            else:
                ic('***** pwd FALSE *****')
                return JsonResponse({
                    'result': 'FAIL',
                    'message': '비밀번호를 확인해주세요.'
                }, status=201)
        except MemberVO.DoesNotExist:
            ic('***** ID is NONE ****')
            return JsonResponse({
                'result': 'FAIL',
                'message': '존재하지 않는 ID 입니다.'
            }, status=201)
        # return HttpResponse(status=104)
    elif request.method == 'PUT':
        data = request.data['body']
        ic(data)
        update_member = data['member']
        ic(update_member)
        pk = update_member['username']
        member = MemberVO.objects.get(pk=pk)
        # user_change_password = update_member['password']
        # ic(user_change_password)
        serializer = MemberVOSerializer(member, data=update_member, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberVOSerializer()
        return JsonResponse(serializer.data, safe=False)
