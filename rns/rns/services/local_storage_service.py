
from django.conf import settings

from rns.services.storage_service import StorageService

class LocalStorage(StorageService):
    def __init__(self):
        super().__init__()

    def upload_file(self, file):
        encrypted_file = self._encrypt_file(file)

        with open(f'{settings.UPLOAD_DIR}/{self.key}', 'wb') as f:
            f.write(encrypted_file)
        
        return f'File uploaded successfully!'