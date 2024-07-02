# Generated by Django 5.0.2 on 2024-06-28 20:02

import plataforma.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0003_alter_noticias_imagen_cabecera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagen_cabecera',
            field=models.ImageField(blank=True, null=True, upload_to='Noticias/28-06-2024/', validators=[plataforma.models.validate_file_extension]),
        ),
    ]