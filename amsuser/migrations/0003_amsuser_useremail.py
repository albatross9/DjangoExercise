# Generated by Django 2.2.4 on 2019-09-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amsuser', '0002_auto_20190906_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='amsuser',
            name='useremail',
            field=models.EmailField(default='test@ruu.kr', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
