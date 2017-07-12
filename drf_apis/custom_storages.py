from django.conf import settings
from django.utils.encoding import filepath_to_uri
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

    def url(self, name, headers=None, response_headers=None, expire=None):
        return '{}{}'.format(settings.STATIC_URL,filepath_to_uri(name))


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

    def url(self, name, headers=None, response_headers=None, expire=None):
        return '{}{}'.format(settings.MEDIA_URL, filepath_to_uri(name))
