# Generated by Django 3.1.3 on 2020-11-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojamariabonita', '0002_auto_20201123_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
