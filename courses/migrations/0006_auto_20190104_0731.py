# Generated by Django 2.1.4 on 2019-01-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190104_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[(' ', 'Please select Level'), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('hnd', 'Higher National Diploma (HND)'), ('degree', 'Degree')], max_length=50),
        ),
    ]
