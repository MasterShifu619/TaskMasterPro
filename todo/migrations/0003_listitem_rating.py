# Generated by Django 4.1.1 on 2024-11-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_listitem_finished_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='rating',
            field=models.IntegerField(default=2),
        ),
    ]
