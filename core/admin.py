from django.contrib import admin
from django.db import models
from .models import Featured_Products, Latest_Products, Newsletter

# Register your models here.
admin.site.register(Featured_Products)
admin.site.register(Latest_Products)
admin.site.register(Newsletter)


