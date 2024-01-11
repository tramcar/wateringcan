from django.shortcuts import get_object_or_404, render

import markdown

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
