# Generated by Django 5.0.2 on 2024-06-28 20:02

import atencion_poblacion.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion_poblacion', '0004_alter_atencionpoblacion_adjunto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencionpoblacion',
            name='adjunto',
            field=models.FileField(blank=True, null=True, upload_to='AtencionPoblacion/28-06-2024/', validators=[atencion_poblacion.models.validate_file_extension]),
        ),
    ]
