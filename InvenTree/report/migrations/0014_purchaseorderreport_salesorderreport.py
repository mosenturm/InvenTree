# Generated by Django 3.0.7 on 2021-03-10 05:46

import django.core.validators
from django.db import migrations, models
import report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_testreport_include_installed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Template name', max_length=100, verbose_name='Name')),
                ('template', models.FileField(help_text='Report template file', upload_to=report.models.rename_template, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html', 'htm'])], verbose_name='Template')),
                ('description', models.CharField(help_text='Report template description', max_length=250, verbose_name='Description')),
                ('revision', models.PositiveIntegerField(default=1, editable=False, help_text='Report revision number (auto-increments)', verbose_name='Revision')),
                ('enabled', models.BooleanField(default=True, help_text='Report template is enabled', verbose_name='Enabled')),
                ('filters', models.CharField(blank=True, help_text='Purchase order query filters', max_length=250, validators=[report.models.validate_purchase_order_filters], verbose_name='Filters')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrderReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Template name', max_length=100, verbose_name='Name')),
                ('template', models.FileField(help_text='Report template file', upload_to=report.models.rename_template, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html', 'htm'])], verbose_name='Template')),
                ('description', models.CharField(help_text='Report template description', max_length=250, verbose_name='Description')),
                ('revision', models.PositiveIntegerField(default=1, editable=False, help_text='Report revision number (auto-increments)', verbose_name='Revision')),
                ('enabled', models.BooleanField(default=True, help_text='Report template is enabled', verbose_name='Enabled')),
                ('filters', models.CharField(blank=True, help_text='Sales order query filters', max_length=250, validators=[report.models.validate_sales_order_filters], verbose_name='Filters')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]