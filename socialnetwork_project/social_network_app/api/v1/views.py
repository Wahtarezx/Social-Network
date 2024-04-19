from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
    get_object_or_404
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from social_network_app.models import Publications, Like, Comments, Reposts
from social_network_app.api.v1.serialisers import (PublicationsSerializer, PublicationsCreateSerializer,
                                                   CommentSerializer, RepostSerializer)
from social_network_app.permissions import IsOwnerOrReadOnly

from django.utils.translation import gettext_lazy as _


class PublicationsListView(ListAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    permission_classes = [IsAuthenticated]


class PublicationsCreateView(CreateAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsCreateSerializer
    permission_classes = [IsAuthenticated]


class PublicationsDetailView(RetrieveDestroyAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PublicationsUpdateView(UpdateAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class LikePublicationView(APIView):
    def post(self, request, pk):
        publication = get_object_or_404(Publications, pk=pk)
        user = request.user
        if Like.objects.filter(user=user, publication=publication).exists():
            like = get_object_or_404(Like, user=user, publication=publication)
            like.delete()
            unlike_message = _('You unliked this publication')
            return Response({"detail": unlike_message}, status=status.HTTP_200_OK)

        Like.objects.create(user=user, publication=publication)
        like_message = _('You liked this publication')
        return Response({"detail": like_message}, status=status.HTTP_200_OK)


class CommentPublicationView(APIView):
    def post(self, request, pk):
        publication = get_object_or_404(Publications, pk=pk)
        user = request.user
        text = request.data['text']
        Comments.objects.create(user=user, text=text, publication=publication)
        comment_message = _('You commented this publication')
        return Response({'detail': f'{comment_message} №{publication.pk}'},
                        status=status.HTTP_200_OK)


class CommentPublicationsListView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get_queryset(self):
        publication_pk = self.kwargs['pub_pk']
        return Comments.objects.filter(publication__pk=publication_pk)


class CommentPublicationDetailView(RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        publication_pk = self.kwargs['pub_pk']
        return Comments.objects.filter(publication__pk=publication_pk)


class Repost(ModelViewSet):
    queryset = Reposts.objects.all()
    serializer_class = RepostSerializer
    permission_classes = [IsOwnerOrReadOnly]
