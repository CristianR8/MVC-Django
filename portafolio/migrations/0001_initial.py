# Generated by Django 4.1.5 on 2023-01-31 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.ImageField(upload_to='portafolio/imagenes/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]