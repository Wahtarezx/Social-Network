from django.urls import path, include


urlpatterns = [
    path('v1/', include('myauth.api.v1.urls'))
]
