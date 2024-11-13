# Generated by Django 5.1.3 on 2024-11-12 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="restaurant name"),
                ),
                ("address", models.TextField(verbose_name="restaurant address")),
                (
                    "phone_number",
                    models.CharField(max_length=13, verbose_name="phone number"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="restaurant_images", verbose_name="restaurant image"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurants",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
