# Generated by Django 4.0.4 on 2022-05-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colBox', '0007_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Selfies', 'Selfies'), ('Food', 'Food'), ('Cars', 'Cars'), ('Swimming', 'Swimming'), ('Football', 'Football'), ('Parks', 'Parks'), ('Forest', 'Forest'), ('Buildings', 'Buildings')], max_length=40),
        ),
    ]
