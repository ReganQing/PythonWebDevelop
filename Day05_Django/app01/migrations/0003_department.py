# Generated by Django 4.1.7 on 2023-02-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_alter_userinfo_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("title", models.CharField(max_length=16)),
            ],
        ),
    ]
