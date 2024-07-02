# Generated by Django 5.0.2 on 2024-06-24 22:59

import atencion_poblacion.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtencionPoblacion',
            fields=[
                ('tramitegeneral_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='plataforma.tramitegeneral')),
                ('nombre', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('carnet', models.CharField(max_length=11)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=250)),
                ('municipality', models.CharField(choices=[('Antilla', 'Antilla'), ('Banes', 'Banes'), ('Báguano', 'Báguano'), ('Cacocum', 'Cacocum'), ('Calixto García', 'Calixto García'), ('Cueto', 'Cueto'), ('Frank País', 'Frank País'), ('Gibara', 'Gibara'), ('Holguín', 'Holguín'), ('Mayarí', 'Mayarí'), ('Moa', 'Moa'), ('Rafael Freyre', 'Rafael Freyre'), ('Sagua de Tánamo', 'Sagua de Tánamo'), ('Urbano Noris', 'Urbano Noris')], max_length=250)),
                ('consulta', models.CharField(choices=[('Duda', 'Duda'), ('Queja', 'Queja'), ('Solicitid de Información', 'Solicitid de Información')], max_length=250)),
                ('adjunto', models.FileField(blank=True, null=True, upload_to='AtencionPoblacion/24-06-2024/', validators=[atencion_poblacion.models.validate_file_extension])),
                ('asunto', models.CharField(max_length=250)),
                ('mensaje', models.TextField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('estado', models.CharField(choices=[('En espera', 'En espera'), ('Aceptado', 'Aceptado'), ('Procesando', 'Procesando'), ('Listo para recoger', 'Listo para recoger'), ('Entregado', 'Entregado'), ('Completado', 'Completado')], default='En espera', max_length=255)),
            ],
            options={
                'verbose_name': 'atención a la población',
                'verbose_name_plural': 'atención a la población',
            },
            bases=('plataforma.tramitegeneral',),
        ),
    ]