
from rns.services.storage_service import StorageService

class LocalStorage(StorageService):
    def __init__(self):
        super().__init__()

    def upload_file(self, file):
        encrypted_file = self._encrypt_file(file)

        with open(f'files/{encrypted_file.name}', 'wb') as f:
            f.write(encrypted_file.read())
        
        return f'File uploaded successfully!'