# Generated by Django 4.2.10 on 2024-03-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insti_app", "0006_paymentmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mentee",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=200)),
                ("contact", models.CharField(max_length=200)),
                ("coaching", models.CharField(max_length=200)),
                ("year_of_study", models.CharField(max_length=20)),
                ("verified", models.BooleanField(default=False)),
            ],
        ),
    ]
