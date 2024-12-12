from apps.BASE.views import ListAPIViewSet
from apps.ADMIN.models import Event
from apps.WEBSITE.serializers import CertificateReadSerializer

class CertificateListAPIView(ListAPIViewSet):
    filterset_fields = ["title","status"]
    queryset = Event.objects.all().order_by("-created")
    serializer_class = CertificateReadSerializer