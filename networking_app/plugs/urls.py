from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlugRequestViewSet, MessageViewSet, Root

router = DefaultRouter()
router.register(r'plug-requests', PlugRequestViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'', Root)


urlpatterns = [
    path('', include(router.urls)),
]
