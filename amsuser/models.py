from django.db import models

# Create your models here.


class Amsuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')

    password = models.CharField(max_length=64, verbose_name='비밀번호')

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Albatross9_AMSuser'
        verbose_name = 'ams 사용자'
        verbose_name_plural = '사용자'
