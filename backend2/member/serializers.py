from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import MemberVO as member


class MemberVOSerializer(serializers.ModelSerializer):
    # username = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = member
        fields = '__all__'
        # fields = ("username", "password", "name", "email")
        # extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return member.objects.create(**validated_data)  # ** -> dictionary

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = ['username']


class LoginSerializer(serializers.BaseSerializer):
    username = serializers.ReadOnlyField(source='member.username')
    password = serializers.ReadOnlyField(source='member.password')

    class Meta:
        model = member
        fields = ['username', 'password']

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log")

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password", "name", "email")
#         # extra_kwargs = {"password": {"write_only": True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data["username"], None, validated_data["password"]
#         )
#         return user


# class MemberCreateSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     name = serializers.CharField()
#     email = serializers.EmailField()
#
#     def create(self, validated_data):
#         member = Member.objects.create(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             name=validated_data['name'],
#             email=validated_data['email'],
#         )
#         member.save()
#         return member


# class MemberSerializer(serializers.Serializer):
#     # username = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
#     username = serializers.CharField(max_length=10)
#     password = serializers.CharField(max_length=10)
#     name = serializers.CharField(max_length=12)
#     email = serializers.EmailField()
#
#     # def get_serializer_context(self):
#     #     return self.context['request'].data
#
#     def create(self, validated_data):
#         # request_data = dict(self.get_serializer_context())
#         # mem_req_data = {'username': request_data['username'][0],
#         #                  'password': request_data['password'][0],
#         #                  'name': request_data['name'][0],
#         #                  'email': request_data['email'][0]}
#         # member_serializer = MemberSerializer(data=mem_req_data)
#         # if member_serializer.is_valid():
#         #     member_serializer.save()
#         return Member.objects.create(**validated_data)  # ** -> dictionary
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance


# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = ['username', 'password', 'name', 'email']
#         # fields = '__all__'



