# Generated by Django 2.2.3 on 2019-07-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_auto_20190712_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempoaluno',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transalunofinanceira',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transalunomatricula',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transalunonota',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transalunopresenca',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tempoaluno',
            name='data',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='transalunofinanceira',
            name='data',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='transalunomatricula',
            name='data',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='transalunonota',
            name='data',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='transalunopresenca',
            name='data',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
