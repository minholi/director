# Generated by Django 2.2.3 on 2019-08-01 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('acoes', '0001_initial'), ('acoes', '0002_auto_20190730_1218')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('alunos', models.BooleanField(default=False)),
                ('inscritos', models.BooleanField(default=False)),
                ('contatos', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'tipo de ação',
                'verbose_name_plural': 'tipos de ações',
            },
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('ativa', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acoes.TipoAcao')),
            ],
            options={
                'verbose_name': 'ação',
                'verbose_name_plural': 'ações',
            },
        ),
    ]
