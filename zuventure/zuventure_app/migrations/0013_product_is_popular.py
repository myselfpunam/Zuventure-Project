# Generated by Django 5.1.4 on 2025-01-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuventure_app', '0012_alter_gallery_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]
