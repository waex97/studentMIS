# Generated by Django 2.1.4 on 2019-01-02 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181224_1854'),
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together={('name', 'course')},
        ),
    ]