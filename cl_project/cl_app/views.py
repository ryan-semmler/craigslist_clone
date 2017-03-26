from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Posting, Category  # , User
from django.contrib.auth.models import User


def home(request):
    template = loader.get_template('cl_app/home.html')
    return HttpResponse(template.render())


def new_listing(request):
    template = loader.get_template('cl_app/new_listing.html')
    return HttpResponse(template.render())


def listing_detail(request, listing_id):
    l = Posting.objects.get(id=listing_id)
    context = {'l': l, }
    template = loader.get_template('cl_app/listing.html')
    return HttpResponse(template.render(context, request))


def city(request):
    template = loader.get_template('cl_app/city.html')
    return HttpResponse(template.render())


def categories(request):
    cats = Category.objects.filter(parent_category=None)
    context = {'cats': cats, 'Category': Category, }
    template = loader.get_template('cl_app/categories.html')
    return HttpResponse(template.render(context, request))


def user_listings(request, user_id):
    listings = Posting.objects.filter(user=user_id)
    u = User.objects.get(id=user_id)
    context = {'listings': listings, 'u': u, }
    template = loader.get_template('cl_app/user_listings.html')
    return HttpResponse(template.render(context, request))
