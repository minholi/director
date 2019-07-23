# Generated by Django 2.2.3 on 2019-07-22 23:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('captacao', '0002_auto_20190722_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='origem',
            options={'verbose_name_plural': 'origens'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'status'},
        ),
        migrations.AddField(
            model_name='lead',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True, verbose_name='atualização'),
        ),
        migrations.AddField(
            model_name='lead',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='criação'),
            preserve_default=False,
        ),
    ]
