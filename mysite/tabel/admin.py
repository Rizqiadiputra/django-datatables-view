# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person, Student
# Register your models here.
admin.site.register(Person),
admin.site.register(Student),