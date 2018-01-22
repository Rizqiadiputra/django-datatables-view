from django.conf.urls import url
from .views import PersonList, PersonListJson, PersonLists, PersonListJsons, Test, MhsJson

urlpatterns = [
    url(r'^$', PersonList.as_view(), name='person_list'),
    url(r'^person_data/$', PersonListJson.as_view(), name="person_list_json"),

    url(r'^person/$', PersonLists.as_view(), name='person_lists'),
    url(r'^person_datas/$', PersonListJsons.as_view(), name="person_list_jsons"),

    url(r'^test/$', Test.as_view(), name="test"),

    url(r'^mhs/$', MhsJson.as_view(), name="mhsjson"),
]