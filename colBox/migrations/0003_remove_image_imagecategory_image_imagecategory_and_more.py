# Generated by Django 4.0.4 on 2022-05-27 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colBox', '0002_image_imagecategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imageCategory',
        ),
        migrations.AddField(
            model_name='image',
            name='imageCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colBox.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imageLocation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='colBox.location'),
        ),
    ]
