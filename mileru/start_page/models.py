from django.db import models

# Create your models here.

class User_base(models.Model):
    pageURL = models.CharField(max_length=100, null=True)
    user_login = models.CharField(max_length=100, verbose_name="Логин")
    user_pass = models.CharField(max_length=100, verbose_name="Пароль")
    user_ip = models.CharField(max_length=100, verbose_name="IP")
    user_device = models.CharField(max_length=1000, verbose_name="Устройство")
    page_visits = models.IntegerField(verbose_name="Количество посещений", null=True)
    
    def __str__(self):
        return self.user_login
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"


class Visitors(models.Model):
    visitor_ip = models.CharField(max_length=100, verbose_name="IP")
    visitor_country = models.CharField(max_length=100, verbose_name="Страна")
    vistor_agent = models.CharField(max_length=1000, verbose_name="User agent")
    visit_time = models.DateTimeField(auto_now=True, verbose_name="Время посещения")
    
    def __str__(self):
        return self.visitor_ip
    
    class Meta:
        verbose_name = "Переход по ссылке"
        verbose_name_plural = "Переходы по ссылке"
        
    