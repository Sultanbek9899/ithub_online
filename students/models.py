from django.contrib.auth.models import User
from django.db import models
from courses.models import Course


class CourseStudent(models.Model):
    """Модель записавшихся на курсы"""
    course_user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='course_owner',
                                         verbose_name='Владелец курса')
    course = models.ForeignKey(Course, on_delete=models.PROTECT,related_name='courses', verbose_name='Название курса')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')  # статус покупки

    class Meta:
        ordering = ['-created']
        verbose_name = 'Студент курса'
        verbose_name_plural = 'Студенты курсов'
        unique_together = [['course_user', 'course']]

    def __str__(self):
        return '{} курсы {}'.format(self.course, self.course_user)