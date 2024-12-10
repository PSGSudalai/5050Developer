from apps.BASE.base import AppAPIView
from apps.WEBSITE.serializers import EventWebReadSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Event


class EventWebListViewSet(ListAPIViewSet):
    queryset=Event.objects.all().order_by("-created")
    serializer_class=EventWebReadSerializer



class EventVideoAPIView(AppAPIView):
    def get(self, request, uuid, *args, **kwargs):
        try:
            event = Event.objects.get(uuid=uuid)
            
            # Extract video data in a serializable format
            video_data = {
                "id": event.video.id if event.video else None,
                "url": event.video.file.url if event.video and event.video.file else None,
            }
            
            data = {
                "uuid": str(event.uuid),
                "title":event.title, # Ensure UUID is converted to string
                "video": video_data,
                "about":event.about,
                "description": event.description,
                "keyskill": event.keyskill,
            }
            return self.send_response({"message": "Event retrieved successfully", "data": data})

        except Event.DoesNotExist:
            return self.send_error_response({"error": "Event not found"})
        except Exception as e:
            return self.send_error_response({"error": str(e)})
