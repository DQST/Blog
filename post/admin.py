from django.contrib import admin
from post import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass
