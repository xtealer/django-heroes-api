from django.contrib import admin

# defined models
from .models import Hero

# register models
admin.site.register(Hero)
