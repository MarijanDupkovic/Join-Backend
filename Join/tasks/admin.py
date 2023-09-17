from django.contrib import admin

from .models import CategoryItem, ContactItem, TaskItem

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(ContactItem)
admin.site.register(CategoryItem)