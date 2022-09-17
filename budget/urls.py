
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import ActionViewSet, JournalViewSet

router = DefaultRouter()
router.register('actions', ActionViewSet, basename='actions')
router.register('journals', JournalViewSet, basename='journals')



urlpatterns = [
    path('', include(router.urls)),


]
