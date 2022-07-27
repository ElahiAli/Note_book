from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'notes'

router = DefaultRouter()
router.register('notes',views.NotesViewSet,basename='note')
urlpatterns = router.urls