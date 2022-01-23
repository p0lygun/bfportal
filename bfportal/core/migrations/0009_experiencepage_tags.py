# Generated by Django 3.2.11 on 2022-01-17 18:04

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('core', '0008_auto_20220117_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='Some tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]