from django.contrib import admin
from .models import Profile,Project,Rating,technologies,categories
# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rating)
admin.site.register(categories)
admin.site.register(technologies)