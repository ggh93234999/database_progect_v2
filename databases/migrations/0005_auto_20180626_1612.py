# Generated by Django 2.0.4 on 2018-06-26 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0004_auto_20180626_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='deleted_at',
            new_name='created_at',
        ),
    ]