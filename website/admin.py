from django import forms
from django.contrib import admin
from django.db import models
from website.models import Config, Nav, Page, Post, Social, Work


class BaseAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '//cdn.ckeditor.com/4.13.1/standard/ckeditor.js',
            'website/js/custom-admin.js'
        )

        css = {
            'all' : ('website/styles/custom-admin.css',),
        }


class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


admin.site.register(Config, ConfigAdmin)
admin.site.register(Nav)
admin.site.register(Page, BaseAdmin)
admin.site.register(Post)
admin.site.register(Work)
admin.site.register(Social)
