# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='عکس کارت دانشجویی')
    title = forms.CharField(label='نام مستعار', max_length=100)
    content = forms.CharField(label='هرچه دل تنگت میخواهد',widget=forms.Textarea)


