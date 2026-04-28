from django.contrib import admin

# Register your models here.
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password", "bio")


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "is_completed",
        "priority",
        "user",
        "created_at",
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Todo, TodoAdmin)
