

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rns.utils.get_storage_service import get_storage_service
from rns.forms import UploadForm

@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']

            storage_service = get_storage_service()
            storage_service.upload_file(file)
            key_used = storage_service.key

            return JsonResponse({'message': 'File uploaded and encrypted successfully!', 'key': key_used.decode()}, status=200)
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})
