# -*-coding:utf-8-*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
class CategoryFile(models.Model):
    class Meta:
        verbose_name = 'Категория файла'
        verbose_name_plural = 'Категории файлов'

    title = models.CharField(verbose_name='Название', max_length=200)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей '
    title = models.CharField(verbose_name='Название', max_length=200)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return str(self.title)

class UploadFileForm(models.Model):
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    title = models.CharField('Название файла', max_length=200)
    about = models.TextField('О файле')
    file = models.FileField(verbose_name='Выберите файл ',upload_to='files/', null=True, blank=True)
    category = models.ForeignKey(  CategoryFile ,verbose_name="Категория" , null=True , blank=True)

    def __str__(self):
        return self.title

# Форма заполнения поста

class Blog(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    image = models.ImageField(upload_to='image/',verbose_name='Изображение к статье', null=True, blank=True)
    author = models.ForeignKey('auth.User' , verbose_name='Автор')
    title = models.CharField(max_length=200 , verbose_name='Заголовок')
    text = models.TextField(verbose_name='Новость')
    category = models.ForeignKey('Category', verbose_name='Категория')
    date_create = models.DateTimeField(default=timezone.now() ,verbose_name='Дата создания')

    minutes = 0
    pages = 5
    def __str__(self):
        return self.title

    def time_read(self):
        probel = 0

        for i in range(len(self.text)):
            if self.text[i] == ' ':
                probel += 1
            if probel == 130:
                self.minutes += 1
                probel = 0
        return self.minutes + 1

    def short_text(self):
        if len(self.text) > 1000:
            return self.text[:1000] + ' ' + '...'

    def get_absolute_url(self):
        return '/articles/%i/' % self.id



# Форма для добавления преподавателей

class add_teacher(models.Model):
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
    image = models.ImageField(upload_to='image/', verbose_name='Image', null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="Ф.И.О")
    email = models.EmailField()
    work_number = models.CharField(max_length=200,verbose_name='Рабочий телефон')
    rank = models.CharField(max_length=200,verbose_name='Звание')
    power = models.CharField(max_length=200,verbose_name='Степень')
    adress = models.CharField(max_length=200,verbose_name='Адресс')
    personal_account = models.CharField(max_length=200,verbose_name='Персональная страница')
    about = models.TextField('О преподавателе' ,null=True, blank=True)


    def __str__(self):
        return self.name




class Time_table(models.Model):
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
    name = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to='image/', verbose_name='Расписание')

    def __str__(self):
        return self.name

class Documentation(models.Model):
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
    title = models.CharField(max_length=200 , verbose_name= 'Название документа')
    about = models.TextField('О файле',null=True, blank=True)
    file = models.FileField(verbose_name='Выберите документ',upload_to='files/documents')