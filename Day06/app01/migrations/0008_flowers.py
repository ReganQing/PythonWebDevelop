# Generated by Django 4.1.7 on 2023-03-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0007_alter_bot_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="Flowers",
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
                ("name", models.CharField(max_length=64, verbose_name="鲜花名称")),
                ("price", models.CharField(max_length=32, verbose_name="价格")),
                ("num", models.IntegerField(verbose_name="销售数量")),
                ("img", models.CharField(max_length=128, verbose_name="形状")),
            ],
        ),
    ]
