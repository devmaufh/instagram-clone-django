# Generated by Django 2.2.2 on 2020-10-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
