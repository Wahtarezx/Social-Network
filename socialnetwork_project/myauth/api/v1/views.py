from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from myauth.api.v1.serializers import RegisterSerializer, UserSerializer

from myauth.permissions import IsOwnerOrReadOnly


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class SubscribeUserAPIView(APIView):
    def post(self, request, pk, format=None):
        try:
            user_to_subscribe = get_user_model().objects.get(pk=pk)
        except get_user_model().DoesNotExist:
            return Response({"error": "Пользователь с указанным pk не найден"}, status=status.HTTP_404_NOT_FOUND)

        current_user = request.user

        if current_user.pk == user_to_subscribe.pk:
            return Response(
                {"error": "Нельзя подписаться на самого себя"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if current_user.subscriptions.filter(pk=user_to_subscribe.pk).exists():
            current_user.subscriptions.remove(user_to_subscribe)
            user_to_subscribe.subscribers.remove(current_user)

            return Response(
                {"success": "Вы успешно отписались от пользователя с pk {}".format(pk)},
                status=status.HTTP_200_OK
            )

        user_to_subscribe.subscribers.add(current_user)
        current_user.subscriptions.add(user_to_subscribe)

        subject = 'Social Network'
        message = (
            f'Уважаемый {user_to_subscribe.first_name}, поздравляем! У вас появился новый поклонник,'
            f' его зовут {current_user.username}. '
        )
        recipient_list = [user_to_subscribe.email]

        send_mail(subject, message, None, recipient_list)

        return Response(
            {"success": "Вы успешно подписались на пользователя с pk {}, ему на почту придет письмо".format(pk)},
            status=status.HTTP_200_OK
        )
