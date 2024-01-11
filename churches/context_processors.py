from .models import Page


def build_menu(request):
    pages = Page.objects.filter(order__gt=0).values('title', 'slug')

    return {'pages': pages}
