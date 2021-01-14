# Generated by Django 3.0.7 on 2020-12-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0024_auto_20201201_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='target_date',
            field=models.DateField(blank=True, help_text='Target date for build completion. Build will be overdue after this date.', null=True, verbose_name='Target completion date'),
        ),
    ]