# Generated by Django 3.0.4 on 2020-03-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='https://i.ya-webdesign.com/images/default-image-png-1.png', upload_to=''),
        ),
    ]