from django.urls import path

from .views import *

urlpatterns = [
    # path('', main_index, name='main_content'),
    path('about_js/', about_js, name='about_js'),
    path('my_courses/', my_courses, name='my_courses_list'),
    path('course/', CoursesList.as_view(), name='courses_list'),
    path('course/<slug:course_slug>/', course_detail, name='course_detail'),
    path('course/<slug:course_slug>/<int:content_id>/',
         course_detail,
         name='course_selected_content')

]