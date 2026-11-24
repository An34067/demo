from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# User = settings['AUTH_USER_MODEL']
# Create your models here.

class Doctor(models.Model):
    full_name = models.CharField()

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"

class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервивы"
    
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=[
        ('new', 'Новая'),
        ('confirmed', 'Подтверждено'),
        ('complited', 'Завершено')
    ])
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "запросы"

class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(blank=True, null=True)
