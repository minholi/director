# Generated by Django 2.2.3 on 2019-07-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academico', '0004_auto_20190711_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('alunos', models.BooleanField(default=False)),
                ('candidatos', models.BooleanField(default=False)),
                ('leads', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'tipo',
            },
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('ativa', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.TipoAcao')),
            ],
            options={
                'verbose_name': 'ação',
                'verbose_name_plural': 'ações',
            },
        ),
        migrations.CreateModel(
            name='AcaoAluno',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('relacionamento.tipoacao',),
        ),
        migrations.CreateModel(
            name='AtendimentoAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('obs', models.TextField(blank=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Aluno')),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamento.AcaoAluno')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
