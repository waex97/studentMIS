# Generated by Django 2.1.4 on 2019-01-06 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batch', '0002_auto_20190102_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reg_fee', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batch.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('', 'Please select your title'), ('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Rev', 'Rev'), ('Dr', 'Dr')], max_length=15)),
                ('initals', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')])),
                ('email', models.EmailField(max_length=255)),
                ('register', models.ManyToManyField(through='student.Registration', to='batch.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
