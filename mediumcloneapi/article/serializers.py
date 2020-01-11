from rest_framework import serializers


from .models import Article

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

class ArticleSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    thumbnail = serializers.CharField()
    # Author = serializers.CharField()
    Author_id = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.Author_id = validated_data.get('author_id', instance.Author_id)

        instance.save()
        return instance