# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from .forms import UploadFileForm
from .models import Document
from django.db import models


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            print(str(request.FILES['file']))

            newdoc = Document(file = request.FILES['file'])
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            newdoc.save()

        else:
            print("nashod")
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


