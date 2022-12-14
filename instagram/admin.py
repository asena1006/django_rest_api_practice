from django.contrib import admin

# Register your models here.
from instagram.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['message']
    list_display = ['pk','message','author']
    pass