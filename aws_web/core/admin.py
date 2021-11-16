from django.contrib import admin

# Register your models here.
from .models import Advertiser,Channel

admin.site.register(Advertiser)
admin.site.register(Channel)
