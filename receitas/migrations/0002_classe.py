# Generated by Django 4.1.2 on 2022-10-15 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receitas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
    ]
