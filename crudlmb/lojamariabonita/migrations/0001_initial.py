# Generated by Django 3.1.3 on 2020-11-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('pontuacao', models.IntegerField(blank=True, null=True)),
                ('habilitado', models.BooleanField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
