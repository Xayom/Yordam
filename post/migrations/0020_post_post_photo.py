# Generated by Django 2.0.3 on 2018-05-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_remove_post_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_photo',
            field=models.ImageField(default=1, upload_to='photo', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]