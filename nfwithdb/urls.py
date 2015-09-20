from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.nfMenu, name='nfmenu'),
    url(r'^read/', views.nfRead, name='nfread'),
    url(r'^rev/',views.nfRevMenu, name='nfrevmenu'),
]