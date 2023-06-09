# Generated by Django 4.2.1 on 2023-06-02 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('detalle', models.CharField(max_length=50)),
                ('fecha_envio', models.DateField()),
                ('nivel', models.CharField(choices=[('GEN', 'General'), ('PRE', 'Ciclo Preescolar'), ('BAS', 'Ciclo Básico'), ('MED', 'Ciclo Medio')], max_length=3)),
                ('fecha_ultima_modificacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
