# Generated by Django 4.0 on 2024-02-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]