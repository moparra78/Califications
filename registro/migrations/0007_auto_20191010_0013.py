# Generated by Django 2.2.5 on 2019-10-10 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20191009_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='materia',
        ),
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Docente'),
        ),
    ]
