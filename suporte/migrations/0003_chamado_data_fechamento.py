# Generated by Django 2.2.3 on 2019-08-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suporte', '0002_auto_20190809_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='data_fechamento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data do fechamento'),
        ),
    ]
