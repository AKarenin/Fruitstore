# Generated by Django 4.2.2 on 2023-07-01 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fruitstore", "0002_fruitstore_rating_alter_fruitstore_phonenumber_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fruitmenu",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fruitMenus",
                to="fruitstore.fruitstore",
            ),
        ),
    ]