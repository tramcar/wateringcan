from .models import Page


def build_menu(request):
    pages = Page.objects.values('title', 'slug')

    return {'pages': pages}
