# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    expertise = models.TextField()

class Student(models.Model):
    nama = models.CharField(max_length=200)
    umur = models.CharField(max_length=10)
    prodi = models.CharField(max_length=50)
