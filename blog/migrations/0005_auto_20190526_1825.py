# Generated by Django 2.1.5 on 2019-05-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190526_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsarticle',
            name='photo',
            field=models.ImageField(default='photo.jpg', upload_to=''),
        ),
    ]
