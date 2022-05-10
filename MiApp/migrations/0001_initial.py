# Generated by Django 4.0.4 on 2022-05-10 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=30)),
                ('student_name', models.CharField(max_length=30)),
                ('student_surname', models.CharField(max_length=30)),
                ('grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('document', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('school_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=30)),
                ('teacher_surname', models.CharField(max_length=30)),
                ('day', models.CharField(max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]