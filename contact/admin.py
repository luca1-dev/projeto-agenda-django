from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'category',)
    search_fields = ('first_name', 'category', 'phone_number',)
    list_per_page = 30
    list_max_show_all = 300