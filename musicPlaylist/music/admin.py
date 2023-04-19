from django.contrib import admin


# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'authorName', 'producedAtDate', 'createdAt', 'updatedAt')
    prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Music, MusicAdmin)
