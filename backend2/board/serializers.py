from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    content = serializers.TextField()
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return instance+validated_data
