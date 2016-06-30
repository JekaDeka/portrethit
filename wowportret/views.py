# -*- coding: utf-8 -*-
from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render
from django.template import loader, Context
from django.db.models import Q

from wowportret.forms import ContactForm, ItemForm
from wowportret.models import Document, Post
from galleryserve.models import Gallery, Item


def main_page(request):
    # form_class, sended = get_form(request)
    # if sended:
    #     return redirect('thank_page')

    # return render(request, 'wowportret/index.html', {'form': form_class})
    return redirect('http://wowportret24.ru/')


def art_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/art.html', {'form': form_class})


def classic_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/classic.html', {'form': form_class})


def holst_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/holst.html', {'form': form_class})


def maslo_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/maslo.html', {'form': form_class})


def maslo2_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/pmaslo.html', {'form': form_class})


def popart_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/popart.html', {'form': form_class})


def portret_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    return render(request, 'wowportret/portret.html', {'form': form_class})


def baget_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    # parent is gallery with bagets
    gal_list = Gallery.objects.filter(parent=65)
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
    return render(request, 'wowportret/gallery/baget.html', {'galleries': galleries, 'form': form_class})


def thank_page(request):
    return render(request, 'wowportret/components/thank.html', {})


def item_page(request, pk):
    form_class, sended = get_item_form(request)
    if sended:
        return redirect('thank_page')

    try:
        item = Item.objects.get(id=pk)
        # Smelly fix for gallery wich parent is Baget_border
        baget_items = Item.objects.filter(
            Q(gallery_id=66) | Q(gallery_id=67) | Q(gallery_id=68)).order_by('id')
    except:
        #raise Http404
        item = Item
        baget_items = Item.objects.all()[:10]

    if (item.gallery_id == 66) or (item.gallery_id == 67) or (item.gallery_id == 68):
        return render(request, 'wowportret/gallery/baget_item.html', {'item': item, 'form': form_class})
    else:
        return render(request, 'wowportret/gallery/gallery_item.html', {'item': item, 'form': form_class, 'baget_items': baget_items})


def gallery_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    gal_list = Gallery.objects.filter(Q(parent=None)).exclude(id=65)
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
    return render(request, 'wowportret/gallery/gallery.html', {'galleries': galleries, 'form': form_class})
    # return render(request, 'wowportret/gallery.html', {'gallery_name':
    # gal.title, 'items': items})


def gallery_detail(request, pk):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    # gal = get_object_or_404(Gallery, pk=pk)
    gal_list = Gallery.objects.filter(parent=pk)
    items = Item.objects.filter(gallery_id=pk)

    paginator = Paginator(items, 12)
    page = request.GET.get('page')

    try:
        gal_items = paginator.page(page)
    except PageNotAnInteger:
        gal_items = paginator.page(1)
    except EmptyPage:
        gal_items = paginator.page(paginator.num_pages)

    if pk == 65:  # if parent of gallery is baget page
        return render(request, 'wowportret/gallery/baget.html', {'galleries': gal_list, 'items': gal_items, 'form': form_class})
    else:
        return render(request, 'wowportret/gallery/gallery.html', {'galleries': gal_list, 'items': gal_items, 'form': form_class})


def get_form(request):
    form_class = ContactForm
    sended = False
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            # template of mail
            content = "name: " + contact_name + "\n"
            content = "phone " + contact_phone + "\n"
            content += "email " + contact_email + "\n"
            content += "text " + form_content + "\n"

            email = EmailMessage(
                "kateart@wowportret.ru",
                content,
                "kateart@wowportret.ru" + '',
                ['kateart222@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            if request.FILES:
                image = request.FILES['docfile']
                newdoc = Document(docfile=image)
                newdoc.save()
                email.attach_file(newdoc.docfile.path)

            email.send()
            sended = True
    return form_class, sended


def get_item_form(request):
    form_class = ItemForm
    sended = False
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_phone = form.cleaned_data['contact_phone']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']
            contact_item = form.cleaned_data['contact_item']

            # template of mail
            content = "name: " + contact_name + "\n"
            content = "phone " + contact_phone + "\n"
            content += "email " + contact_email + "\n"
            content += "text " + form_content + "\n"
            content += "extra:  " + contact_item + "\n"

            email = EmailMessage(
                "kateart@wowportret.ru",
                content,
                "kateart@wowportret.ru" + '',
                ['kateart222@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            if request.FILES:
                image = request.FILES['docfile']
                newdoc = Document(docfile=image)
                newdoc.save()
                email.attach_file(newdoc.docfile.path)

            email.send()
            sended = True
    return form_class, sended


def post_list(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'wowportret/blog/post_list.html', {'posts': posts, 'form': form_class})


def post_detail(request, pk):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'wowportret/blog/post_detail.html', {'post': post, 'form': form_class})
