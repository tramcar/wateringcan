from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import ContactUsForm
from .models import Page


def index(request):
    page = get_object_or_404(Page, order=0)
    return render(request, "wateringcan/index.html", {"page": page})


def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, "wateringcan/detail.html", {"page": page})


def detail_slug(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    return render(request, "wateringcan/detail.html", {"page": page})


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = "[%s] Site feedback" % (settings.CHURCH_NAME)
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            recipients = [settings.CHURCH_EMAIL_ADDRESS]

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect("/")
    else:
        form = ContactUsForm()

    return render(request, "wateringcan/contact_us.html", {"form": form})
