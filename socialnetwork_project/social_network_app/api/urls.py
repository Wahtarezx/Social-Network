from django.urls import path
from social_network_app.api.v1.views import (
    PublicationsListView,
    PublicationsDetailView,
    PublicationsCreateView,
    PublicationsUpdateView,
    LikePublicationView,
    CommentPublicationView,
    CommentPublicationsListView,
    CommentPublicationDetailView,
)


app_name = 'social_network_app'

urlpatterns = [
    path('publications/', PublicationsListView.as_view(), name='publications'),
    path('publications/create/', PublicationsCreateView.as_view(), name='publications_create'),
    path('publications/<int:pk>/', PublicationsDetailView.as_view(), name='publications_detail'),
    path('publications/<int:pk>/update/', PublicationsUpdateView.as_view(), name='publications_update'),
    path('publications/<int:pk>/like/', LikePublicationView.as_view(), name='like'),
    path('publications/<int:pk>/comment/', CommentPublicationView.as_view(), name='comment'),
    path('publications/<int:pub_pk>/comments_list/', CommentPublicationsListView.as_view(), name='comments_list'),
    path('publications/<int:pub_pk>/comments_list/<int:pk>/', CommentPublicationDetailView.as_view(),
         name='comment_delete')
]