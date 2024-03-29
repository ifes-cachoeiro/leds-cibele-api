# Generated by Django 4.1.2 on 2023-05-25 16:51

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('registration', models.CharField(max_length=30, verbose_name='Matrícula')),
                ('key', models.CharField(help_text='Hash identificador do funcionário', max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('base_settings', djongo.models.fields.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceAcademicsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('access_period', djongo.models.fields.JSONField()),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.academicmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('settings', djongo.models.fields.JSONField()),
                ('academics', models.ManyToManyField(blank=True, help_text='Membros com permissões de acesso', through='api.DeviceAcademicsModel', to='api.academicmodel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=120)),
                ('floor', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('log', djongo.models.fields.JSONField()),
                ('academic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.academicmodel')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.devicemodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.locationmodel'),
        ),
        migrations.AddField(
            model_name='deviceacademicsmodel',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.devicemodel'),
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome coordenadoria')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.locationmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='academicmodel',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.departmentmodel', verbose_name='Departamento/Coordenadoria'),
        ),
    ]
