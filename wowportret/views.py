from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse


def main_page(request):
    return render(request, 'wowportret/index.html', {})


def art_page(request):
    return render(request, 'wowportret/art.html', {})


def classic_page(request):
    return render(request, 'wowportret/classic.html', {})


def holst_page(request):
    return render(request, 'wowportret/holst.html', {})


def index_page(request):
    return render(request, 'wowportret/index.html', {})


def maslo_page(request):
    return render(request, 'wowportret/maslo.html', {})


def maslo2_page(request):
    return render(request, 'wowportret/pmaslo.html', {})


def popart_page(request):
    return render(request, 'wowportret/popart.html', {})


def portret_page(request):
    return render(request, 'wowportret/portret.html', {})
