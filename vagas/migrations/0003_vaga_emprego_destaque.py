# Generated by Django 3.2.12 on 2022-03-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0002_alter_vaga_emprego_experiencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga_emprego',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]
