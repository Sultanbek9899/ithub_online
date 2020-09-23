from django.contrib import admin

from .models import  Course, Module, Content


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['course',  'title', 'order']
    list_filter = ["order", 'course']
    search_fields = ['title', 'order']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'module']
    list_filter = ['module']
    search_fields = ['title']


