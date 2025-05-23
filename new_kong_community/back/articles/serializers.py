from rest_framework import serializers
from .models import Article
from .models import Comment

class ArticleTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['title']

class ArticleListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    movie = ArticleTitleSerializer(read_only=True) 

    class Meta:
        model = Article
        fields = ['id', 'movie', 'title', 'content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
