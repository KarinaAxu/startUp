# Generated by Django 4.2.15 on 2024-10-21 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={
                "ordering": ["created_at"],
                "permissions": (("can_view_dish", "Can view dish"),),
                "verbose_name_plural": "dishes",
            },
        ),
    ]
