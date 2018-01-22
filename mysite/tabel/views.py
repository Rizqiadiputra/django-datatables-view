# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from .models import Person, Student
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
# Create your views here.
# def person_list(request):
#     persons = Person.objects.all()
#     return render(request, 'tabel/person_list.html',{'personalia':persons})



class MhsJson(BaseDatatableView):
    model = Student
    columns = ['nama', 'umur', 'prodi']
    order_columns = ['nama', 'umur', 'prodi']

class PersonList(TemplateView):
    template_name = 'tabel/person_list.html'
    
class PersonListJson(BaseDatatableView):
    model = Person
    # model = User
    columns = ['name','company','expertise']
    order_columns = ['name','company','expertise']
    # columns = ['username','email','expertise']
    # order_columns = ['username','email','expertise']

class PersonLists(TemplateView):
    template_name = 'tabel/person_lists.html'

class PersonListJsons(BaseDatatableView):
    model = Person
    # model = User
    columns = ['name','company','expertise']
    order_columns = ['name','company','expertise']
    # columns = ['username','email','expertise']
    # order_columns = ['username','email','expertise']

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(name__istartswith=sSearch) | Q(company__istartswith=sSearch) | Q(expertise__istartswith=sSearch))
        return qs

class Test(TemplateView):
    template_name = 'tabel/test.html'