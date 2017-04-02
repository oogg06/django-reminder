from django.contrib import admin

# Register your models here.

from .models import EmailAccount, GMailAccount

admin.site.register(EmailAccount)
admin.site.register(GMailAccount)