from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Prefetch, Sum
from django.utils import timezone
from datetime import timedelta
from django.db import transaction, IntegrityError

from .models import Post, Comment, Like, KarmaTransaction
from .serializers import PostSerializer

@api_view(['GET'])
def feed(request):
    posts = Post.objects.select_related('author').prefetch_related(
        Prefetch(
            'comments',
            queryset=Comment.objects.select_related('author').prefetch_related('replies')
        )
    )
    return Response(PostSerializer(posts, many=True).data)

@api_view(['POST'])
def like_post(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)

    with transaction.atomic():
        try:
            Like.objects.create(user=user, post=post)
            KarmaTransaction.objects.create(user=post.author, points=5, source='POST_LIKE')
        except IntegrityError:
            pass

    return Response({"status": "ok"})

@api_view(['GET'])
def leaderboard(request):
    last_24h = timezone.now() - timedelta(hours=24)
    data = (
        KarmaTransaction.objects.filter(created_at__gte=last_24h)
        .values('user__username')
        .annotate(total_karma=Sum('points'))
        .order_by('-total_karma')[:5]
    )
    return Response(data)
