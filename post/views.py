from rest_framework import viewsets, views, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from post import models
from post import serializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.order_by('-created')
    serializer_class = serializer.PostViewSetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get('uid', self.request.user.pk)
        return self.queryset.filter(user_id=user_id)


class FollowAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uid):
        if request.user.id == uid:
            return Response(data={'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        if models.Subscribe.objects.filter(follower=request.user, following_id=uid).exists():
            return Response(data={'error': 'You already follow'}, status=status.HTTP_400_BAD_REQUEST)

        models.Subscribe.objects.create(follower=request.user, following_id=uid)
        return Response(data={'status': 'ok'}, status=status.HTTP_201_CREATED)


class UnfollowAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uid):
        models.Subscribe.objects.filter(follower=request.user, following_id=uid).delete()
        return Response(data={'status': 'ok'}, status=status.HTTP_200_OK)
