from django.contrib import admin


from .models import CourseStudent
# Register your models here.


@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ['paid', 'created']
    list_filter = ['paid', 'created', 'course']
    search_fields = [ 'created']