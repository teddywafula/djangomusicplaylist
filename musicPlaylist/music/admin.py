from django.contrib import admin
from .models import Music


# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'authorName', 'producedAtDate', 'createdAt', 'updatedAt')


admin.site.register(Music, MusicAdmin)
