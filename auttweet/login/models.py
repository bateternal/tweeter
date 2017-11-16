# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='login/media')

