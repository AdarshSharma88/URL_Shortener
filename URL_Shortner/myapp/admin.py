from django.contrib import admin
# Register your models here.
from .models import LongToShort, UserAuthentication


admin.site.register((LongToShort, UserAuthentication))
