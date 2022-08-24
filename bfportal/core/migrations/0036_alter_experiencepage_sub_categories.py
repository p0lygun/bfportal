# Generated by Django 3.2.12 on 2022-08-24 16:52

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0035_alter_experiencepage_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experiencepage",
            name="sub_categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True,
                help_text="Choose Sub Category Category",
                null=True,
                to="core.SubCategory",
            ),
        ),
    ]
