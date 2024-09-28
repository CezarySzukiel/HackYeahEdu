from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CustomUser
from .serializers import StudentUserDetailsSerializer


class UserListView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = StudentUserDetailsSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = StudentUserDetailsSerializer
