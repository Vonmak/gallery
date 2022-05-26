# Generated by Django 4.0.4 on 2022-05-26 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('imageName', models.CharField(max_length=70)),
                ('imageDescription', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('imageLocation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='colBox.location')),
            ],
        ),
    ]
