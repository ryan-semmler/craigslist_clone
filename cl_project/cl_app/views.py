from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Posting


def home(request):
    template = loader.get_template('cl_app/home.html')
    return HttpResponse(template.render())


def new_listing(request):
    template = loader.get_template('cl_app/new_listing.html')
    return HttpResponse(template.render())


def listing_detail(request, listing_id):
    l = Posting.objects.get(id=listing_id)
    context = {'l': l, }
    template = loader.get_template('cl_app/listing')
    return HttpResponse(template, render(context, request))
