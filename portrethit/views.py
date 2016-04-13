from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse


def main_page(request):
    return render(request, 'portrethit/index.html', {})
