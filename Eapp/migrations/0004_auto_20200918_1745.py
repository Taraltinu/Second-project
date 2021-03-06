# Generated by Django 3.1.1 on 2020-09-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0003_registrationmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationmodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='added_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='occupation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='profil_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='registrationmodel',
            name='update_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
