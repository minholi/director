# Generated by Django 2.2.4 on 2019-08-12 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacionamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobranca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cobranca', models.IntegerField(unique=True)),
                ('tipo', models.CharField(max_length=20)),
                ('ano', models.DecimalField(decimal_places=0, max_digits=4)),
                ('mes', models.DecimalField(decimal_places=0, max_digits=2)),
                ('data_venc', models.DateField(verbose_name='data de venc.')),
                ('data_pgto', models.DateField(blank=True, null=True, verbose_name='data de pgto.')),
                ('val_orig', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='val. orig.')),
                ('val_final', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='val. final')),
                ('val_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='val. pago')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamento.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('ano', models.DecimalField(decimal_places=0, max_digits=4)),
                ('periodo', models.DecimalField(decimal_places=0, max_digits=2)),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3)),
                ('situacao', models.CharField(max_length=20)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamento.Aluno')),
            ],
            options={
                'unique_together': {('disciplina', 'aluno')},
            },
        ),
    ]
