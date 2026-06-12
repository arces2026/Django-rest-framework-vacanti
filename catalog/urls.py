from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutoreViewSet


router = DefaultRouter()
router.register('libri', LibroViewSet)
router.register('autori', AutoreViewSet)

urlpatterns = router.urls