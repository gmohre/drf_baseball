from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from drf_apis.drf_baseball.urls import urlpatterns as baseball_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
urlpatterns += baseball_urls
#May need to update this
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
