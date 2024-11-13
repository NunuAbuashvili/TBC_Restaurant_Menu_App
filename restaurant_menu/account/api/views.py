from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSignupSerializer


class UserSignupAPIView(CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = (~IsAuthenticated,)
