# Generated by Django 5.1.4 on 2025-01-09 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zuventure_app', '0018_companyinfo_facebook_url_companyinfo_instagram_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='linkdin_url',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
