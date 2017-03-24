from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_listing$', views.new_listing, name='new_listing'),
    url(r'^city$', views.city, name='city'),
    url(r'^categories$', views.categories, name='categories'),
    url(r'^listing_(?P<listing_id>[0-9]+)$', views.listing_detail, name='listing_detail'),
]
