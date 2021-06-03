from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import RequestClient
from .models import RequestImages
from datetime import datetime
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

# Create your views here.
from django.db import models


def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            # save info to model
            saveModelClient(request)
            pathImg = '/media/' + request.FILES['file'].name
            return HttpResponse("Good" + pathImg)
        else:
            return HttpResponse("Bad" + request.FILES['file'].name)

    form = UploadFileForm()
    return render(request, 'fileUploaderTemplate.html', {'form': form})


def saveModelClient(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    fullname = request.POST['fullname']
    className = request.POST['classname']

    modelSave = RequestClient(client_name=fullname,
                              class_name=className,
                              number_image=1,
                              create_at=dt_string, status=1, result_client=-1)
    modelSave.save()
    # save model to request image
    saveModelImage(request, modelSave)


def saveModelImage(request, parentRequest):
    pathImg = 'media/' + request.FILES['file'].name
    pk = parentRequest.pk
    status = 1
    result = -1

    f = open(pathImg, 'r')
    requestImage = RequestClient(image_path=File(f),
                                 request_image_id=pk,
                                 status=status,
                                 result_image=result)
    requestImage.save()


def upload(f):
    file = open('media/' + f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
