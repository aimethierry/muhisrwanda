from django.conf.urls import url
from . import views
from .views import (
    CategoryListView
)

urlpatterns = [
    url(r'^$', views.home, name="index"),
    # url(r'^gallery/$', CategoryListView.as_view(), name="gallery"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),

]
