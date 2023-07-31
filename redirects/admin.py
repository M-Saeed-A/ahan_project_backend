from django.contrib import admin

from .models import Redirect

class RedirectAdmin(admin.ModelAdmin):
    list_display = ('request_url','destination_url')
    list_filter = ('created', 'updated', 'status_code')
    search_fields = ('request_url', 'destination_url')


admin.site.register(Redirect, RedirectAdmin)