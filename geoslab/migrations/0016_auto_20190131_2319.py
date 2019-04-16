# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-01 04:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('geoslab', '0015_auto_20190128_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image1_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image10',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image10_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image2_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image3_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image4',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image4_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image5',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image5_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image6',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image6_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image7',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image7_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image8',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image8_project', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='image9',
            field=filer.fields.image.FilerImageField(blank=True, default=None, help_text='Please supply an image for this project', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image9_project', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
