from django import template
from website.models import Config, Nav, Social

register = template.Library()


@register.simple_tag
def get_navs():
    navs = list(Nav.objects.all().order_by('order'))
    return navs


@register.simple_tag
def is_active(request, current):
    if request.path.replace('/', '') == current:
        return 'active'

@register.simple_tag
def get_config():
    config = Config.objects.all().first()
    return config

@register.simple_tag
def get_socials():
    socials = list(Social.objects.all().order_by('order'))
    return socials
