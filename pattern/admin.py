from django.contrib.admin import site

from pattern.models import *

site.register (Pattern)
site.register (Language)
site.register (Use)
site.register (Implementation)
site.register (Tags)