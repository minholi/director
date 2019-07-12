# Generated by Django 2.2.3 on 2019-07-12 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_auto_20190711_1054'),
        ('log', '0008_auto_20190711_1641'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tempoaluno',
            unique_together={('aluno', 'data')},
        ),
        migrations.AlterUniqueTogether(
            name='transalunofinanceira',
            unique_together={('aluno', 'data')},
        ),
        migrations.AlterUniqueTogether(
            name='transalunomatricula',
            unique_together={('aluno', 'data')},
        ),
        migrations.AlterUniqueTogether(
            name='transalunonota',
            unique_together={('aluno', 'data')},
        ),
        migrations.AlterUniqueTogether(
            name='transalunopresenca',
            unique_together={('aluno', 'data')},
        ),
    ]
