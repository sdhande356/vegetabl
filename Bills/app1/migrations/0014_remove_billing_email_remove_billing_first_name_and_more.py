# Generated by Django 4.1.3 on 2022-11-21 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_billing_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='email',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='billing',
            name='mobile',
        ),
    ]
