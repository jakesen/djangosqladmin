from django.conf.urls import url
from djangosqladmin.databases import views

urlpatterns = [
    url(r'^$', views.dashboard)
]
