# Generated by Django 2.2.3 on 2019-07-29 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('ra', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='RA')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('curso', models.CharField(max_length=255)),
                ('curriculo', models.CharField(max_length=40, verbose_name='currículo')),
                ('serie', models.IntegerField(verbose_name='série')),
                ('polo', models.CharField(max_length=255)),
                ('criacao', models.DateTimeField(auto_now_add=True, verbose_name='criação')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='atualização')),
            ],
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('acoes.acao',),
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Presenca', verbose_name='conversão')),
            ],
            options={
                'verbose_name': 'presença',
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Nota', verbose_name='conversão')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Matricula', verbose_name='conversão')),
            ],
            options={
                'verbose_name': 'matrícula',
            },
        ),
        migrations.CreateModel(
            name='Financeira',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Financeira', verbose_name='conversão')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Documentacao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Documentacao', verbose_name='conversão')),
            ],
            options={
                'verbose_name': 'documentação',
                'verbose_name_plural': 'documentação',
            },
        ),
        migrations.CreateModel(
            name='Cadastral',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Cadastral', verbose_name='conversão')),
            ],
            options={
                'verbose_name_plural': 'cadastrais',
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Atividade', verbose_name='conversão')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('obs', models.TextField(blank=True)),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='relacionamento.Acao')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamento.Aluno')),
            ],
            options={
                'verbose_name': 'atendimento',
            },
        ),
        migrations.CreateModel(
            name='Andamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('situacao', models.CharField(max_length=40, verbose_name='situação')),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
                ('conversivel', models.BooleanField(default=False, verbose_name='conversível')),
                ('conversao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Andamento', verbose_name='conversão')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='andamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Andamento'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Cadastral', verbose_name='situação'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='documentacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Documentacao', verbose_name='documentação'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='financeira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Financeira'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Matricula', verbose_name='matrícula'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Nota'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='presenca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='relacionamento.Presenca', verbose_name='presença'),
        ),
    ]
