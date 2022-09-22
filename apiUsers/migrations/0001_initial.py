# Generated by Django 4.1.1 on 2022-09-08 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('contraseña', models.CharField(max_length=25)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('fecha_de_nacimiento', models.DateField()),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.genero')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=25)),
                ('fecha_de_nacimiento', models.DateField()),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('registro', models.CharField(max_length=20)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.especialidad')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=25)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiUsers.genero')),
            ],
        ),
    ]
