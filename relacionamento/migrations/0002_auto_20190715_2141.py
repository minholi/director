# Generated by Django 2.2.3 on 2019-07-16 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relacionamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimentoaluno',
            options={'verbose_name': 'atendimento'},
        ),
        migrations.AlterModelOptions(
            name='tipoacao',
            options={'verbose_name': 'tipo de ação', 'verbose_name_plural': 'tipos de ações'},
        ),
    ]
