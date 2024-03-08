from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
    get_object_or_404
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Publications, Like, Comments
from .serialisers import PublicationsSerializer, PublicationsCreateSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


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
            return Response({"detail": "Вы уже поставили лайк на эту публикацию."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            Like.objects.create(user=user, publication=publication)
            return Response({"detail": "Вы поставили лайк на эту публикацию."}, status=status.HTTP_200_OK)


class UnlikePublicationView(APIView):
    def post(self, request, pk):
        publication = get_object_or_404(Publications, pk=pk)
        user = request.user
        like = get_object_or_404(Like, user=user, publication=publication)
        like.delete()
        return Response({"detail": "Вы убрали лайк с этой публикации."}, status=status.HTTP_200_OK)


class CommentPublicationView(APIView):
    def post(self, request, pk):
        publication = get_object_or_404(Publications, pk=pk)
        user = request.user
        text = request.data['text']
        Comments.objects.create(user=user, text=text, publication=publication)
        return Response({'detail': f'Вы оставили комментарий для публикации №{publication.pk}'},
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

    def get_queryset(self):
        publication_pk = self.kwargs['pub_pk']
        return Comments.objects.filter(publication__pk=publication_pk)


