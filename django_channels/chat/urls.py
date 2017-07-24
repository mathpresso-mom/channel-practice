from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[A-z0-9]{8}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{12})/$', views.chat_room,
        name='chat_room'),
]
