# Generated by Django 4.0.4 on 2022-05-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(),
        ),
    ]
