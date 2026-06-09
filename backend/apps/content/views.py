from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Episode, Guest, Article, Subscriber
from .serializers import EpisodeSerializer, GuestSerializer, ArticleSerializer, SubscriberSerializer

@api_view(['GET'])
def home_data(request):
    featured = Episode.objects.filter(status=Episode.PUBLISHED, featured=True).first() or Episode.objects.filter(status=Episode.PUBLISHED).first()
    latest = Episode.objects.filter(status=Episode.PUBLISHED)[:6]
    guests = Guest.objects.filter(featured=True)[:6]
    articles = Article.objects.filter(published=True)[:3]
    return Response({
        'featured': EpisodeSerializer(featured).data if featured else None,
        'latest': EpisodeSerializer(latest, many=True).data,
        'guests': GuestSerializer(guests, many=True).data,
        'articles': ArticleSerializer(articles, many=True).data,
    })

@api_view(['GET'])
def episodes_list(request):
    q = request.GET.get('q', '')
    episodes = Episode.objects.filter(status=Episode.PUBLISHED)
    if q:
        episodes = episodes.filter(title__icontains=q)
    return Response(EpisodeSerializer(episodes, many=True).data)

@api_view(['GET'])
def episode_detail(request, slug):
    try:
        episode = Episode.objects.get(slug=slug, status=Episode.PUBLISHED)
    except Episode.DoesNotExist:
        return Response({'detail': 'Episodio no encontrado'}, status=404)
    related = Episode.objects.filter(status=Episode.PUBLISHED).exclude(id=episode.id)[:3]
    return Response({'episode': EpisodeSerializer(episode).data, 'related': EpisodeSerializer(related, many=True).data})

@api_view(['GET'])
def guests_list(request):
    return Response(GuestSerializer(Guest.objects.all(), many=True).data)

@api_view(['GET'])
def articles_list(request):
    return Response(ArticleSerializer(Article.objects.filter(published=True), many=True).data)

@api_view(['POST'])
def subscribe(request):
    serializer = SubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'ok': True, 'message': 'Suscripción registrada'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
