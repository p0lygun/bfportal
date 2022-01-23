# Generated by Django 3.2.11 on 2022-01-17 18:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('core', '0009_experiencepage_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperiencePageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='core.experiencepage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_experiencepagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='ExperienceTag',
        ),
        migrations.AlterField(
            model_name='experiencepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='Some tags', through='core.ExperiencePageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]