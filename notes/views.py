from .permissions import IsAdminOrReadOnly
from .serializers import NotesSerializer
from .models import Notes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class NotesViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAdminOrReadOnly,IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)