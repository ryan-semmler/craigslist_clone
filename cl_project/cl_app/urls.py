from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_listing$', views.new_listing, name='new_listing'),
    # url(r'^city$', views.city, name='city'),
]
