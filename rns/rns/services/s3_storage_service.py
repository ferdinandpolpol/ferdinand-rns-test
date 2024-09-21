
import boto3

from django.conf import settings

from rns.services.storage_service import StorageService


class S3Storage(StorageService):
    def __init__(self):
        super().__init__()

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
    
    def upload_file(self, file):
        encrypted_file = self._encrypt_file(file)

        try:
            with open(f'files/{encrypted_file.name}', 'wb') as f:
                self.s3.put_object(Bucket=settings.AWS_S3_BUCKET_NAME, Key=file.name, Body=f.read())
        except Exception as e:
            # TODO: Be more specific with the exception
            raise Exception(f'Error uploading file: {e}')

        return f'File uploaded successfully!'