# Generated by Django 4.0.1 on 2022-01-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerexame',
            name='exam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='academic.exam'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='status',
            field=models.CharField(choices=[('draft', 'Rascunho'), ('active', 'Ativo')], default='open', max_length=20, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]