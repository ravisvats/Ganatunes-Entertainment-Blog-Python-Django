# Generated by Django 3.1 on 2020-08-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200819_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link above to read the Blog Post', max_length=255),
        ),
    ]
