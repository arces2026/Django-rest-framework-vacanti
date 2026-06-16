from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutoreViewSet
from . import views


router = DefaultRouter()
router.register('libri', LibroViewSet)
router.register('autori', AutoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profilo/', views.profilo, name='profilo'),
]