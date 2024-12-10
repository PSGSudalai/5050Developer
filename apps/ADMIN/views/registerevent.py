from apps.ADMIN.serializers import RegisterEventReadSerializer
from apps.BASE.views import ListAPIViewSet
from apps.ADMIN.models import RegisterEvent

class RegisterEventListAPIView(ListAPIViewSet):
    queryset = RegisterEvent.objects.all()
    serializer_class = RegisterEventReadSerializer
    