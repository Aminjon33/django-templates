from django.contrib import admin
from .models import Blog, Category, Contact

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'create_date',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Contact)

