# Generated by Django 2.2.3 on 2019-07-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='andamento',
            options={'verbose_name': 'sit. de andamento', 'verbose_name_plural': 'sit. de andamento'},
        ),
        migrations.AlterModelOptions(
            name='desempenho',
            options={'verbose_name': 'sit. de desempenho', 'verbose_name_plural': 'sit. de desempenho'},
        ),
        migrations.AlterModelOptions(
            name='presenca',
            options={'verbose_name': 'sit. de presença', 'verbose_name_plural': 'sit. de presença'},
        ),
        migrations.AddField(
            model_name='aluno',
            name='polo',
            field=models.CharField(default='Umuarama', max_length=255),
            preserve_default=False,
        ),
    ]
