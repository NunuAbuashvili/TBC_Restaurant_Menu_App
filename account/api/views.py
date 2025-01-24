from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSignupSerializer


class UserSignupAPIView(CreateAPIView):
    """
    API endpoint that allows users to register.
    Only non-authenticated users can access this endpoint.
    """
    serializer_class = UserSignupSerializer
    permission_classes = (~IsAuthenticated,)
