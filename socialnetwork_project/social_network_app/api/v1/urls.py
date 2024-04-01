from django.urls import path, include
from rest_framework.routers import DefaultRouter
from social_network_app.api.v1.views import (
    PublicationsListView,
    PublicationsDetailView,
    PublicationsCreateView,
    PublicationsUpdateView,
    LikePublicationView,
    CommentPublicationView,
    CommentPublicationsListView,
    CommentPublicationDetailView,
    Repost,
)


router = DefaultRouter()
router.register('repost_list', Repost)


urlpatterns = [
    path('social_network/publications/', PublicationsListView.as_view(), name='publications'),
    path('social_network/publications/create/', PublicationsCreateView.as_view(), name='publications_create'),
    path('social_network/publications/<int:pk>/', PublicationsDetailView.as_view(), name='publications_detail'),
    path('social_network/publications/<int:pk>/update/', PublicationsUpdateView.as_view(), name='publications_update'),
    path('social_network/publications/<int:pk>/like/', LikePublicationView.as_view(), name='like'),
    path('social_network/publications/<int:pk>/comment/', CommentPublicationView.as_view(), name='comment'),
    path('social_network/publications/<int:pub_pk>/comments_list/', CommentPublicationsListView.as_view(),
         name='comments_list'),
    path('social_network/publications/<int:pub_pk>/comments_list/<int:pk>/', CommentPublicationDetailView.as_view(),
         name='comment_delete'),
    path('reposts/', include(router.urls)),
]
