# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView



def home(request):
    return render(request,"home.html")


def gallery(request):
    return render(request, "gallery.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


class CategoryListView(ListView):
	template_name = 'gallery.html'
