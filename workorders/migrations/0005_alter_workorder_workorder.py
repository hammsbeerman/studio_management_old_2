# Generated by Django 3.2.12 on 2022-05-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0004_alter_workorder_workorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='workorder',
            field=models.CharField(max_length=100, verbose_name='Workorder'),
        ),
    ]
