# Generated by Django 3.0.4 on 2020-03-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200319_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default-image.png', upload_to=''),
        ),
    ]
