# Generated by Django 3.2.6 on 2021-08-03 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_subscription', '0003_auto_20210803_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subscribe_categories',
            new_name='category',
        ),
    ]