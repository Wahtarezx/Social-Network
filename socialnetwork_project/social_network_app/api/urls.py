from django.urls import path, include


urlpatterns = [
    path('v1/', include('social_network_app.api.v1.urls'))
]
