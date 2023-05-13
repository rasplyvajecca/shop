from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    email = models.CharField('Почта')
    about = models.CharField('Описание', max_length=50)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
