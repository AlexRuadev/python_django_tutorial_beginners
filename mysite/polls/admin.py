from django.contrib import admin

# from this directory, go to models, and import the Question model
from .models import Question

# Register your models here.
admin.site.register(Question)
