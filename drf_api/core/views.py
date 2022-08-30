from .models import Core
from .serializers import CoreSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CoreList(ListCreateAPIView):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer


class CoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Core.objects.all()
    serializer_class = CoreSerializer
