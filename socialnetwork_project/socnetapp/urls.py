from django.urls import path
from .views import (
    PublicationsListView,
    PublicationsDetailView,
    PublicationsCreateView,
    PublicationsUpdateView,
    LikePublicationView,
    UnlikePublicationView,
    CommentPublicationView,
    CommentPublicationsListView,
    CommentPublicationDetailView,
)


app_name = 'socnetapp'

urlpatterns = [
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('publications/create/', PublicationsCreateView.as_view(), name='publications_create'),
    path('publications/<int:pk>/', PublicationsDetailView.as_view(), name='publications_detail'),
    path('publications/<int:pk>/update/', PublicationsUpdateView.as_view(), name='publications_update'),
    path('publications/<int:pk>/like/', LikePublicationView.as_view(), name='like'),
    path('publications/<int:pk>/unlike/', UnlikePublicationView.as_view(), name='unlike'),
    path('publications/<int:pk>/comment/', CommentPublicationView.as_view(), name='comment'),
    path('publications/<int:pub_pk>/commentslist/', CommentPublicationsListView.as_view(), name='commentslist'),
    path('publications/<int:pub_pk>/commentslist/<int:pk>/', CommentPublicationDetailView.as_view(),
         name='comment-delete')
]
