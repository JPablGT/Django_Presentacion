# Generated by Django 4.2.3 on 2023-07-18 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_remove_card_phone_alter_card_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='address',
            new_name='mensaje',
        ),
    ]