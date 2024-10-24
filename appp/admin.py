from django.contrib import admin
from .models import Category, Worker, Menu

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'worker', 'category')
    search_fields = ('worker__name', 'category__name')
    list_filter = ('category',)

# Register the models with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Menu, MenuAdmin)
