from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlugRequestViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'plug-requests', PlugRequestViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
