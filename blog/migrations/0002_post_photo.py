# Generated by Django 4.1.4 on 2023-01-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='no-pic.jpg', upload_to='post_pics'),
        ),
    ]