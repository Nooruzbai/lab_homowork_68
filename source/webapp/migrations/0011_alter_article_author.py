# Generated by Django 4.0 on 2022-01-17 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default='Unknown', max_length=200, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Автор'),
        ),
    ]
