# Generated by Django 3.1.7 on 2021-04-15 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spell', '0010_auto_20210415_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='duration',
            field=models.IntegerField(choices=[(10, 'natychmiastowy'), (12, '1 runda'), (4, '1 minuta'), (5, '10 minut'), (6, '1 godzina'), (7, '8 godzin'), (9, '24 godziny'), (14, '7 dni'), (15, '10 dni'), (16, '30 dni'), (17, 'specjalny'), (11, 'do rozproszenia')], default=1),
        ),
    ]
