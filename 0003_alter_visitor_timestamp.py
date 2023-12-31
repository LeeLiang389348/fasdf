# Generated by Django 4.2.4 on 2023-08-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0002_crime_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
