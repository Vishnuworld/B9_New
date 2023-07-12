from django.contrib import admin
from .models import Book

# Register your models here.


admin.site.register([Book])  # you can add multiple models here in list