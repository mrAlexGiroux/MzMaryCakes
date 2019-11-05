from django.contrib import admin

from .models import Cake, Ingredient,  Comment

admin.site.register(Cake)
admin.site.register(Ingredient)
admin.site.register(Comment)
