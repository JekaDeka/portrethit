# -*- coding: utf-8 -*-
from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render
from django.template import loader, Context


from wowportret.forms import ContactForm
from wowportret.models import Document

from galleryserve.models import Gallery, Item


def main_page(request):
    form_class, sended = get_form(request)
    if sended:
        return redirect('thank_page')

    return render(request, 'wowportret/index.html', {'form': form_class})


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

    gal = get_object_or_404(Gallery, pk=37)
    if gal.has_child != True:
        gal_list = Gallery.objects.all()
        items = Item.objects.filter(gallery__title=gal.title)
        paginator = Paginator(items, 10)
        page = request.GET.get('page')
        try:
            gal_items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            gal_items = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            gal_items = paginator.page(paginator.num_pages)
        # return render(request, 'wowportret/gallery.html', {'galleries':
        # galleries})

        return render(request, 'wowportret/gallery_detail.html', {'galleries': gal_list, 'gallery': gal, 'items': gal_items})
    else:
        gal_list = Gallery.objects.filter(parent=gal.id)
        return render(request, 'wowportret/gallery.html', {'galleries':
                                                           gal_list})


def thank_page(request):
    return render(request, 'wowportret/thank.html', {})


# def gallery_page(request):
#     gal = Gallery
#     return render(request, 'wowportret/gallery.html', {'gallery': gal})


# add image_page
def image_page(reuqest):
    pass


def gallery_page(request):
    gal_list = Gallery.objects.filter(parent=None)
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
    return render(request, 'wowportret/gallery.html', {'galleries': galleries})
    # return render(request, 'wowportret/gallery.html', {'gallery_name':
    # gal.title, 'items': items})


def gallery_detail(request, pk):
    gal = get_object_or_404(Gallery, pk=pk)
    if gal.has_child != True:
        gal_list = Gallery.objects.all()
        items = Item.objects.filter(gallery__title=gal.title)
        paginator = Paginator(items, 10)
        page = request.GET.get('page')
        try:
            gal_items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            gal_items = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            gal_items = paginator.page(paginator.num_pages)
        # return render(request, 'wowportret/gallery.html', {'galleries':
        # galleries})

        return render(request, 'wowportret/gallery_detail.html', {'galleries': gal_list, 'gallery': gal, 'items': gal_items})
    else:
        gal_list = Gallery.objects.filter(parent=gal.id)
        return render(request, 'wowportret/gallery.html', {'galleries':
                                                           gal_list})


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
