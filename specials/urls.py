from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='specials-home'),
    url(r'^about/$', views.about, name='specials-about'),
]

