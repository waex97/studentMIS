# Generated by Django 2.1.4 on 2018-12-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181224_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
