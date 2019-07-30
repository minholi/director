# Generated by Django 2.2.3 on 2019-07-29 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingresso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name_plural': 'status',
            },
        ),
        migrations.AddField(
            model_name='inscrito',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inscrito',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ingresso.Status'),
            preserve_default=False,
        ),
    ]
