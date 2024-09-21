
from django.conf import settings

from rns.services.s3_storage_service import S3Storage
from rns.services.local_storage_service import LocalStorage

def get_storage_service():
    environment = settings.ENVIRONMENT

    if environment == 'production':
        return S3Storage()
    
    return LocalStorage()
    