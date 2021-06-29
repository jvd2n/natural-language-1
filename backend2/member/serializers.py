from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    # username = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'password', 'name', 'email']

    def create(self, validated_data):
        return Member.objects.create(**validated_data)  # ** -> dictionary

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('username', instance.password)
        instance.name = validated_data.get('username', instance.name)
        instance.email = validated_data.get('username', instance.email)
        return instance


# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member
#         fields = ('username')