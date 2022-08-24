# Generated by Django 3.2.12 on 2022-08-24 16:47

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("core", "0033_auto_20220824_1633"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="experiencescategory",
            options={"verbose_name_plural": "Main Categories"},
        ),
        migrations.RemoveField(
            model_name="experiencepage",
            name="categories",
        ),
        migrations.AddField(
            model_name="experiencepage",
            name="category",
            field=models.ForeignKey(
                help_text="Choose Main Category",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="core.experiencescategory",
            ),
        ),
        migrations.AddField(
            model_name="experiencepage",
            name="sub_categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True,
                help_text="Choose Sub Category Category",
                null=True,
                to="core.ExperiencesCategory",
            ),
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=255)),
                (
                    "icon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Sub Categories",
            },
        ),
    ]