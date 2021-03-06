# Generated by Django 3.1.1 on 2020-09-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cover_pic', models.FileField(upload_to='media/%y/%m/%d')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'ContactModel'},
        ),
    ]
