# Generated by Django 2.0 on 2018-02-04 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecocases', '0008_question_esm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='question',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecocases.Question'),
        ),
    ]
