# Generated by Django 4.0.2 on 2022-02-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
