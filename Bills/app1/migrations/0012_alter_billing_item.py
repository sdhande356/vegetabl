# Generated by Django 4.1.3 on 2022-11-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_billing_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='item',
            field=models.CharField(choices=[('0', '---select item----'), ('Potates', '20'), ('Tomotoes', '30'), ('Onion', '30'), ('Cabbage', '40'), ('Apple', '50')], default='0', max_length=50),
        ),
    ]