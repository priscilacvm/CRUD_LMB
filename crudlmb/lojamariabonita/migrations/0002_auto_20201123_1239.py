# Generated by Django 3.1.3 on 2020-11-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojamariabonita', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='observacao',
            new_name='Referencia',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='habilitado',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pontuacao',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Bairro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='CEP',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
