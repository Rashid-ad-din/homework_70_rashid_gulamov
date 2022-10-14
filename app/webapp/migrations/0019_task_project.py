# Generated by Django 4.1.1 on 2022-10-13 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]