# Generated by Django 2.2.8 on 2020-04-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_postmodel_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
