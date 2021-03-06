# -*- coding: utf-8 -*-
from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render
from django.template import loader, Context
from django.db.models import Q
from functools import partial
import re

from wowportret.forms import ContactForm, ItemForm
from wowportret.models import Document, Post
from galleryserve.models import Gallery, Item


def new_page(request, redirect_to):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, redirect_to, {'form': form})


def main_page(request):
    # return new_page(request, 'wowportret/index.html')
    #
    return redirect('http://wowportret24.ru/')


def art_page(request):
    return new_page(request, 'wowportret/art.html')


def test_page(request):
    return new_page(request, 'wowportret/components/test.html')


def classic_page(request):
    return new_page(request, 'wowportret/classic.html')


def holst_page(request):
    return new_page(request, 'wowportret/holst.html')


def maslo_page(request):
    return new_page(request, 'wowportret/maslo.html')


def maslo2_page(request):
    return new_page(request, 'wowportret/pmaslo.html')


def popart_page(request):
    return new_page(request, 'wowportret/popart.html')


def portret_page(request):
    return new_page(request, 'wowportret/portret.html')


def baget_page(request):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    # parent is gallery with bagets
    all_gals = Gallery.objects.filter(is_baget=True)
    gal_list = all_gals.filter(parent=None).order_by('title')
    # item_list = Item.objects.all()
    # paginator = Paginator(gal_list, 9)  # Show 9 galleries per page
    # page = request.GET.get('page')
    # try:
    #     galleries = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     galleries = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     galleries = paginator.page(paginator.num_pages)
    return render(request, 'wowportret/gallery/baget.html', {'all_gals': gal_list, 'galleries': gal_list, 'form': form})


def thank_page(request):
    return render(request, 'wowportret/components/thank.html', {})


def item_page(request, pk):
    form, sended = get_item_form(request)
    if sended:
        return redirect('thank_page')

    try:
        item = Item.objects.get(id=pk)
    except:
        #raise Http404
        item = Item
        baget_items = Item.objects.all()[:10]

    if (item.gallery.is_baget == True):
        all_gals = Gallery.objects.filter(is_baget=True)
        all_gals = all_gals.filter(parent=None).order_by('title')
        return render(request, 'wowportret/gallery/baget_item.html', {'all_gals': all_gals, 'item': item, 'form': form})
    else:
        all_gals = Gallery.objects.filter(is_baget=False)
        all_gals = all_gals.filter(parent=None).order_by('title')
        baget_items = Item.objects.filter(
            Q(gallery_id=66) | Q(gallery_id=67) | Q(gallery_id=68)).order_by('title')
        return render(request, 'wowportret/gallery/gallery_item.html', {'all_gals': all_gals, 'item': item, 'form': form, 'baget_items': baget_items})


def gallery_page(request):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    all_gals = Gallery.objects.filter(is_baget=False)
    gal_list = all_gals.filter(parent=None).order_by('title')
    paginator = Paginator(gal_list, 9)  # Show 9 galleries per page
    page = request.GET.get('page')
    try:
        galleries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        galleries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        galleries = paginator.page(paginator.num_pages)
    return render(request, 'wowportret/gallery/gallery.html', {'all_gals': gal_list, 'galleries': galleries, 'form': form})


def gallery_detail(request, pk):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    gal = get_object_or_404(Gallery, pk=pk)
    gal_list = Gallery.objects.filter(parent=pk)
    items = Item.objects.filter(gallery_id=pk).order_by('title')

    paginator = Paginator(items, 18)
    page = request.GET.get('page')

    try:
        gal_items = paginator.page(page)
    except PageNotAnInteger:
        gal_items = paginator.page(1)
    except EmptyPage:
        gal_items = paginator.page(paginator.num_pages)

    if gal.is_baget == True:  # if parent of gallery is baget page
        if not gal_list:
            gal_list = gal_list = Gallery.objects.filter(id=pk)
        all_gals = Gallery.objects.filter(is_baget=True)
        all_gals = all_gals.filter(parent=None).order_by('title')
        return render(request, 'wowportret/gallery/baget.html', {'all_gals': all_gals, 'galleries': gal_list, 'items': gal_items, 'crnt_gal': gal, 'form': form})
    else:
        all_gals = Gallery.objects.filter(is_baget=False)
        all_gals = all_gals.filter(parent=None).order_by('title')
        return render(request, 'wowportret/gallery/gallery.html', {'all_gals': all_gals, 'galleries': gal_list, 'items': gal_items, 'crnt_gal': gal, 'form': form})


def get_form(request):
    form = ContactForm
    sended = False
    if request.method == 'POST':
        form = form(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            if (re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', contact_phone)):
                # template of mail
                content = "Name: " + contact_name + "\n"
                content += "Phone " + contact_phone + "\n"
                content += "Email: " + contact_email + "\n"
                content += "Message: " + form_content + "\n"

                email = EmailMessage(
                    "kateart@wowportret.ru",
                    content,
                    "kateart@wowportret.ru" + '',
                    ['kateartis22@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                if request.FILES:
                    image = request.FILES['docfile']
                    newdoc = Document(docfile=image)
                    newdoc.save()
                    email.attach_file(newdoc.docfile.path)

                email.send()
                sended = True
    return form, sended


def get_item_form(request):
    form = ItemForm
    sended = False
    if request.method == 'POST':
        form = form(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']
            contact_item = form.cleaned_data['contact_item']
            if (re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', contact_phone)):

                # template of mail
                content = "Name: " + contact_name + "\n"
                content += "Phone: " + contact_phone + "\n"
                content += "Email: " + contact_email + "\n"
                content += "Message: " + form_content + "\n"
                content += "" + contact_item + "\n"

                email = EmailMessage(
                    "kateart@wowportret.ru",
                    content,
                    "kateart@wowportret.ru" + '',
                    ['kateartis22@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                if request.FILES:
                    image = request.FILES['docfile']
                    newdoc = Document(docfile=image)
                    newdoc.save()
                    email.attach_file(newdoc.docfile.path)

                email.send()
                sended = True
    return form, sended


def post_list(request):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'wowportret/blog/post_list.html', {'posts': posts, 'form': form})


def post_detail(request, pk):
    form, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'wowportret/blog/post_detail.html', {'post': post, 'form': form_class})


def price_page(request):
    return new_page(request, 'wowportret/price.html')


def delivery_page(request):
    return new_page(request, 'wowportret/delivery.html')


def payment_page(request):
    return new_page(request, 'wowportret/payment.html')


def contacts_page(request):
    return new_page(request, 'wowportret/contacts.html')
