# Generated by Django 4.2.2 on 2023-07-01 02:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fruitstore", "0003_alter_fruitmenu_store"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fruitmenu",
            old_name="store",
            new_name="fruitStore",
        ),
    ]
