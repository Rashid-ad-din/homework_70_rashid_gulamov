# Generated by Django 4.1.1 on 2022-10-10 16:52

from django.db import migrations, models
import webapp.models.tasks


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=150, validators=[webapp.models.tasks.unique, webapp.models.tasks.CustomValidator()], verbose_name='Заголовок'),
        ),
    ]
