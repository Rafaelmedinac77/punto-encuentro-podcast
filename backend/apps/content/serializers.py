from rest_framework import serializers
from .models import Category, Guest, Episode, Article, Subscriber

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class GuestSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Guest
        fields = ['id', 'name', 'slug', 'profession', 'bio', 'photo_url', 'instagram', 'youtube', 'website', 'featured']
    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else ''

class EpisodeSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    embed_url = serializers.SerializerMethodField()
    class Meta:
        model = Episode
        fields = ['id','title','slug','subtitle','description','youtube_url','youtube_id','embed_url','thumbnail_url','duration','reflection','guest','categories','featured','published_at']
    def get_embed_url(self, obj):
        return f'https://www.youtube.com/embed/{obj.youtube_id}' if obj.youtube_id else ''

class ArticleSerializer(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id','title','slug','excerpt','content','cover_url','created_at']
    def get_cover_url(self, obj):
        return obj.cover.url if obj.cover else ''

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id','name','email']
