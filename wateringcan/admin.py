from django.contrib import admin


from .models import Page


class PageAdmin(admin.ModelAdmin):
    exclude = ('content_html',)


admin.site.register(Page, PageAdmin)
