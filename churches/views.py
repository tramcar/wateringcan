from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


import markdown

from .forms import ContactUsForm
from .models import Page


def index(request):
    page = get_object_or_404(Page, order=0)
    # TODO: Sanitize markdown
    content_md = markdown.markdown(page.content)
    return render(request, "churches/index.html", {"page": page, "content_md": content_md})


def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    # TODO: Sanitize markdown
    content_md = markdown.markdown(page.content)
    return render(request, "churches/detail.html", {"page": page, "content_md": content_md})


def detail_slug(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    # TODO: Sanitize markdown
    content_md = markdown.markdown(page.content)
    return render(request, "churches/detail.html", {"page": page, "content_md": content_md})


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

    return render(request, "churches/contact_us.html", {"form": form})
