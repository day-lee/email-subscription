# Generated by Django 3.2.6 on 2021-08-03 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_subscription', '0002_auto_20210803_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subcribe_categories',
            new_name='subscribe_categories',
        ),
        migrations.RenameField(
            model_name='usersubscription',
            old_name='subcribe_categories',
            new_name='category',
        ),
    ]
