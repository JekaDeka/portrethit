from django.shortcuts import render,  get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect


from wowportret.forms import ContactForm
from wowportret.models import Document


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
    return render(request, 'wowportret/baget.html', {'form': form_class})


def thank_page(request):
    return render(request, 'wowportret/thank.html', {})


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
            image = request.FILES['docfile']

            newdoc = Document(docfile=image)
            newdoc.save()

            # template of mail
            content = "Меня зовут: " + contact_name + "\n"
            content = "Мой телефон " + contact_phone + "\n"
            content += "Моя почта: " + contact_email + "\n"
            content += "Сообщение: " + form_content + "\n"

            email = EmailMessage(
                "wowportret.ru",
                content,
                "wowportret.ru" + '',
                ['ZharkovEvgeniy94@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.attach(image.name, image.read(), image.content_type)
            email.send()
            sended = True
    return form_class, sended
