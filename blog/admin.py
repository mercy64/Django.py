# from django.contrib import admin
# from .models import ExampleModel
#
# # Register your models here.
# class ExampleModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at')  # Customize the columns shown in the list view
#     search_fields = ('name',)  # Add a search bar for specific fields
#
# admin.site.register(ExampleModel, ExampleModelAdmin)

from django.contrib import admin
from .models import ExampleModel

class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name_upper')
    search_fields = ('name',)

admin.site.register(ExampleModel, ExampleModelAdmin)
