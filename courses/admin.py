from django.contrib import admin

# Register your models here.
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at'] #campos da tabela de listagem
    search_fields = ['name', 'slug'] #campos de busca
    prepopulated_fields = {'slug': ('name',)} #popular campo na inserção


admin.site.register(Course, CourseAdmin)
