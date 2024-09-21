
from cryptography.fernet import Fernet

from django.conf import settings



class StorageService:
    key: str = ""

    def __init__(self):
        self.key = Fernet.generate_key()

    def _encrypt_file(self, file):
        fernet = Fernet(self.key)
        encrypted_data = fernet.encrypt(file.read())

        return encrypted_data

    def upload_file(self, file):
        raise NotImplementedError()