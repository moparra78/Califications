# Generated by Django 2.2.5 on 2019-10-10 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20191009_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultad',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='facultad',
            name='materia',
        ),
        migrations.AddField(
            model_name='docente',
            name='facultad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Facultad'),
        ),
        migrations.AddField(
            model_name='materia',
            name='facultad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Facultad'),
        ),
    ]
