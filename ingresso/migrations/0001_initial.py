# Generated by Django 2.2.3 on 2019-07-23 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastral',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ingresso.Cadastral', verbose_name='conversão')),
            ],
            options={
                'verbose_name': 'sit. cadastral',
                'verbose_name_plural': 'sit. cadastrais',
            },
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
            ],
            options={
                'verbose_name': 'ação',
                'verbose_name_plural': 'ações',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('acoes.acao',),
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='código')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('concurso', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=255)),
                ('polo', models.CharField(max_length=255)),
                ('ano', models.CharField(max_length=4)),
                ('periodo', models.CharField(max_length=2)),
                ('criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='atualização')),
                ('cadastral', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ingresso.Cadastral', verbose_name='situação')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('obs', models.TextField(blank=True)),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscritos', to='ingresso.Acao', verbose_name='ação')),
                ('inscrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingresso.Inscrito')),
            ],
            options={
                'verbose_name': 'atendimento',
            },
        ),
    ]
