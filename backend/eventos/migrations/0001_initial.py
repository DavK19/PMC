# Generated by Django 5.1.3 on 2024-11-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=200)),
                ('calificacion', models.FloatField(default=0.0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='eventos')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('eventos', models.ManyToManyField(related_name='usuarios_set', to='eventos.evento')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='usuarios',
            field=models.ManyToManyField(related_name='eventos_set', to='eventos.usuario'),
        ),
    ]
