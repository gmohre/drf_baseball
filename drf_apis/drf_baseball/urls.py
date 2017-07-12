from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import NumpyFunctionViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'^numpy', NumpyFunctionViewSet)
urlpatterns = router.urls
