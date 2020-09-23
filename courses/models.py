from django.db import models
from .fields import OrderField
# Create your models here.
from django.contrib.auth.models import User


class Course(models.Model):
    """Модели для курсов"""
    icon = models.ImageField(upload_to='icons',
                             verbose_name='Иконки курсов',
                             default='static/img/js.png')
    title = models.CharField(max_length=200, verbose_name='Название курса')
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField(verbose_name='Короткое описание', max_length=500,
                                         default='')
    overview = models.TextField(verbose_name='Описание курса')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    status = models.BooleanField(default=False, verbose_name='Доступен ли курс')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class Module(models.Model):
    """ Разделы или категории тем """
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'], verbose_name='Очередной номер раздела')

    class Meta:
        ordering = ['order']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    """Контент часть с видео и файлом"""
    title = models.CharField(max_length=200)
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    order = OrderField(blank=True, for_fields=['module'])
    content_description = models.TextField()
    video_content = models.FileField(upload_to='videos', verbose_name='Видеоурок')
    file_content = models.FileField(upload_to='files', verbose_name='Файлы для урока')

    class Meta:
        ordering = ['order']
        verbose_name = 'Тема/Контент'
        verbose_name_plural = 'Темы/Контент'

    def __str__(self):
        return self.title
