from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView
from .models import Course, Content
# from student.models import CourseStudent
from students.models import CourseStudent


class CoursesList(ListView):
    model = Course
    template_name = 'course_list.html'


@login_required
def course_detail(request, course_slug, content_id=None):
    course = get_object_or_404(Course, slug=course_slug)
    student_course = get_object_or_404(CourseStudent, course=course)
    # проверяем пользователя с купимшим этот курс пользователем , если он есть даем доступ инчае 403
    if request.user == student_course.course_user:
        if content_id:
            content = get_object_or_404(Content, id=content_id)
        else:
            content = get_object_or_404(Content, title='Introduction')
        return render(request,
                      'courses/course_detail.html',
                      {'course': course,
                       'content': content})

    else:
        return redirect("courses_list")


@login_required
def my_courses(request):
    # функция что бы взять все курсы данного пользователя
    all_user_courses = CourseStudent.objects.filter(course_user=request.user)
    return render(request, 'courses/my_curses_list.html', context={'courses': all_user_courses})


def main_index(request):
    return render(request, 'index.html')


def about_js(request):
    return render(request, 'more_js.html')